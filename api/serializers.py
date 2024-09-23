from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import People, QrCode, Seat


class PeopleMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ["ID", "name", "image"]


class SeatSerializer(serializers.ModelSerializer):
    people = PeopleMiniSerializer()

    class Meta:
        model = Seat
        fields = "ID", "name", "image", "people", "has_taken"


class QrCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QrCode
        fields = "__all__"


class PeopleSerializer(serializers.ModelSerializer):
    seat = SeatSerializer()
    qrcode = QrCodeSerializer()

    class Meta:
        model = People
        fields = [
            "ID",
            "user",
            "name",
            "phone_number",
            "passport_data",
            "birthday_date",
            "image",
            "seat",
            "qrcode",
        ]


class UserSerializer(serializers.ModelSerializer):
    people = PeopleSerializer()

    class Meta:
        model = User
        fields = ["username", "people"]

    def update(self, instance, validated_data):
        people_data = validated_data.pop("people", None)
        instance.username = validated_data.get("username", instance.username)
        instance.save()

        if people_data:
            people_instance = instance.people
            people_instance.name = people_data.get("name", people_instance.name)
            people_instance.phone_number = people_data.get(
                "phone_number", people_instance.phone_number
            )
            people_instance.passport_data = people_data.get(
                "passport_data", people_instance.passport_data
            )
            people_instance.birthday_date = people_data.get(
                "birthday_date", people_instance.birthday_date
            )
            people_instance.image = people_data.get(
                "birthday_date", people_instance.image
            )
            people_instance.save()

        return instance


class PeopleIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ("ID",)
