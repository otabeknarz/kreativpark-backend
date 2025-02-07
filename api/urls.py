from django.urls import path, include
from . import views

app_name = "api"

urlpatterns = [
    path("auth/", include("api.auth.urls", namespace="auth")),
    path("people/", views.people_get, name="people_get"),
    path("people/add/", views.people_post, name="people_post"),
    path("people/IDs/", views.people_IDs, name="people_IDs"),
    path("people/check/<str:ID>/", views.people_check, name="people_check"),
    path("qrcode/", views.qrcode_get, name="qrcode_get"),
    path("qrcode/add/", views.qrcode_post, name="qrcode_post"),
    path(
        "qrcode/delete/expired/",
        views.cancel_all_expired_booked_seats,
    ),
    path("qrcode/delete/<str:user_ID>/", views.qrcode_delete, name="qrcode_delete"),
    path("qrcode/check/<str:ID>/", views.qrcode_check, name="qrcode_check"),
    path("login-library/<str:qrcode_ID>/", views.login_library, name="login_library"),
    path(
        "qrcode/people/check/<str:people_id>/",
        views.people_has_qrcode,
        name="people_has_qrcode",
    ),
    path(
        "get-number-token/<str:people_id>/",
        views.get_number_token,
        name="get_number_token",
    ),
    path("get-csrf-token/", views.get_csrf_token, name="get_csrf_token"),
    path("user/", views.get_user, name="user_get"),
    path("user/edit/", views.edit_user, name="user_edit"),
    path("stats/home/", views.stats_home, name="stats_home"),
    path("seats/", views.seat_get, name="seat_get"),
    path("enter-lib/", views.enter_lib, name="enter_lib"),
    path("cancel-booking/", views.cancel_booking, name="cancel_booking"),
]

# Urls for admins

urlpatterns += [
    path("stats/<int:days>/", views.stats, name="stats"),
]
