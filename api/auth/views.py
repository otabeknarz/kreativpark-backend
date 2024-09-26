from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from api.serializers import UserSerializer
from core.models import NumberToken


class CustomTokenView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        code = request.data.get("code")

        if code and len(code) != 6 and code.isdigit():
            return Response(
                {"status": "false", "detail": "Code must be a 6-digit number"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            number_token = NumberToken.objects.get(number_token=code)
        except Exception as e:
            return Response(
                {"status": "false", "detail": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if number_token.is_expired():
            number_token.delete()
            return Response(
                {"status": "false", "detail": "Code has been expired"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        refresh = RefreshToken.for_user(number_token.user)

        number_token.delete()
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": UserSerializer(number_token.user).data,
            },
            status=status.HTTP_200_OK,
        )
