from django.contrib import admin
from .models import (
    Room,
    News,
    MessageFromGuestUser,
    People,
    QrCode,
    Data,
    NumberToken,
    Seat,
)


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = "name", "phone_number", "created_at"
    search_fields = "name", "phone_number"


@admin.register(QrCode)
class QrCodeAdmin(admin.ModelAdmin):
    list_display = "people", "created_at"
    search_fields = ("people",)


@admin.register(Data)
class QrCodeAdmin(admin.ModelAdmin):
    list_display = "people", "purpose", "type", "created_at"
    search_fields = ("people",)


admin.site.register(Room)
admin.site.register(News)
admin.site.register(MessageFromGuestUser)
admin.site.register(NumberToken)
admin.site.register(Seat)
