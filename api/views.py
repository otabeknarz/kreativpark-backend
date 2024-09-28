from rest_framework.permissions import IsAuthenticated

from core.models import People, QrCode, Data, NumberToken, Seat
from datetime import datetime, timedelta
from .serializers import (
    PeopleSerializer,
    QrCodeSerializer,
    PeopleIDSerializer,
    UserSerializer,
    SeatSerializer,
)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

# csrf token
from django.middleware.csrf import get_token


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user(request):
    serializer = UserSerializer(request.user)
    return Response(
        {"user": serializer.data, "status": "true"}, status=status.HTTP_200_OK
    )


@api_view(["PUT", "PATCH"])
@permission_classes([IsAuthenticated])
def edit_user(request):
    serializer = UserSerializer(
        request.user, data=request.data, partial=(request.method == "PATCH")
    )
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"user": serializer.data, "status": "true"}, status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def enter_lib(request):
    seat_id = request.data.get("seat_id")
    try:
        seat = Seat.objects.get(ID=seat_id)
    except Exception as e:
        return Response({"status": "false", "detail": str(e)})
    people = People.objects.get(user=request.user)
    people.seat = seat
    qr_code = QrCode(people=people, type="IN", purpose="Kutubxona")
    qr_code.create_qr_code()
    people.save()
    return Response(
        {
            "status": "true",
            "seat": SeatSerializer(seat).data,
            "qr_code_image": qr_code.image_path,
            "user": UserSerializer(request.user).data,
        },
        status=status.HTTP_200_OK,
    )


# APIs for seat model
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def seat_get(request):
    seats = Seat.objects.all()
    serializer = SeatSerializer(seats, many=True)
    return Response(
        {"status": "true", "seats": serializer.data}, status=status.HTTP_200_OK
    )


# APIs for people model
@api_view(["GET"])
def people_get(request):
    people = People.objects.all()
    serializer = PeopleSerializer(people, many=True)
    return Response({"people_count": people.count(), "people": serializer.data})


@api_view(["POST"])
def people_post(request):
    serializer = PeopleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def people_check(request, ID):
    try:
        people = People.objects.get(ID=ID)
    except People.DoesNotExist:
        return Response({"status": "false"})
    return Response(
        {
            "status": "true",
            "people": {
                "name": str(people.name),
                "ID": str(people.ID),
                "phone_number": str(people.phone_number),
                "created_at": str(people.created_at),
                "updated_at": str(people.updated_at),
            },
        }
    )


@api_view(["GET"])
def people_IDs(request):
    people = PeopleIDSerializer(People.objects.all(), many=True)
    return Response(people.data)


# APIs for QrCode model
@api_view(["GET"])
def qrcode_get(request):
    qrcode = QrCode.objects.all()
    serializer = QrCodeSerializer(qrcode, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def qrcode_delete(request, user_ID):
    try:
        people = People.objects.get(ID=user_ID)
        qrcode = QrCode.objects.get(people=people)
    except Exception as e:
        return Response({"status": "false", "detail": str(e)})
    image_path = qrcode.image_path
    qrcode.delete()
    return Response({"status": "true", "image_path": image_path})


@api_view(["POST"])
def qrcode_post(request):
    serializer = QrCodeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def qrcode_check(request, ID):
    try:
        qrcode = QrCode.objects.get(ID=ID)
    except QrCode.DoesNotExist:
        return Response({"status": "false"})
    return Response(
        {
            "status": "true",
            "qrcode": {
                "people": {"name": qrcode.people.name, "ID": str(qrcode.people.ID)},
                "ID": str(qrcode.ID),
                "created_at": str(qrcode.created_at),
                "type": str(qrcode.type),
                "purpose": str(qrcode.purpose),
                "image_path": str(qrcode.image_path),
            },
        }
    )


@api_view(["GET"])
def people_has_qrcode(request, people_id):
    try:
        people = People.objects.get(ID=people_id)
    except Exception as e:
        return Response({"status": "false", "detail": str(e)})
    try:
        qrcode = QrCode.objects.get(people=people)
    except Exception as e:
        return Response({"status": "false", "detail": str(e)})
    return Response({"status": "true"})


@api_view(["GET"])
def login_library(request, qrcode_ID):
    try:
        qrcode = QrCode.objects.get(ID=qrcode_ID)
    except QrCode.DoesNotExist:
        return Response({"status": "false"})
    data = Data.objects.create(
        people=qrcode.people, purpose=qrcode.purpose, type=qrcode.type
    )
    qrcode.delete()
    return Response({"status": "true"})


# Functions for admins
@api_view(["GET"])
def stats(request, days):
    if days == 0:
        data = Data.objects.filter()
        people = People.objects.filter()
    else:
        ending_date = datetime.today()
        starting_date = ending_date - timedelta(days=days)
        data = Data.objects.filter(created_at__range=[starting_date, ending_date])
        people = People.objects.filter(created_at__range=[starting_date, ending_date])
    people_json = []
    data_json = {}
    for p in people:
        people_dict = {
            "ID": p.ID,
            "name": p.name,
            "phone_number": p.phone_number,
            "passport_data": p.passport_data,
            "created_at": str(p.created_at),
        }
        people_json.append(people_dict)

    data_types = {}

    for d in data:
        data_json["ID"] = d.pk
        data_json["people"] = d.people.ID
        data_json["purpose"] = d.purpose
        data_json["type"] = d.type
        data_json["created_at"] = str(d.created_at)
        if d.purpose != "":
            try:
                data_types[d.purpose] += 1
            except KeyError:
                data_types[d.purpose] = 1

    return Response(
        {
            "people_count": people.count(),
            "data_count_IN": data.filter(type="IN").count(),
            "data_count_OUT": data.filter(type="OUT").count(),
            "purposes": data_types,
            "people": people_json,
        }
    )


# get number token
@api_view(["GET"])
def get_number_token(request, user_id):
    try:
        people = People.objects.get(ID=user_id)
    except Exception as e:
        return Response({"status": "false", "detail": str(e)})

    try:
        people.number_token.delete()
    except Exception as e:
        number_token = NumberToken.objects.create(people=people)
        return Response(
            {"status": "true", "number_token": str(number_token.number_token)}
        )
    number_token = NumberToken.objects.create(people=people)
    return Response({"status": "true", "number_token": str(number_token.number_token)})


@api_view(["GET"])
def get_csrf_token(request):
    return Response({"csrf_token": get_token(request)})