import random

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Room, News, NumberToken
from django.http import JsonResponse


def home(request):
    news_ = News.published.all()[:10]
    rooms_ = Room.objects.all()[:10]
    if request.method == "POST":
        return JsonResponse({"status": "ok"}, safe=False)

    return render(request, "core/home.html", {"news": news_, "rooms": rooms_})


def room(request, slug):
    room_ = get_object_or_404(Room, slug=slug)
    return render(request, "core/room.html", {"room": room_})


def news(request, slug):
    news_ = get_object_or_404(News, slug=slug)
    news_.update_views()
    return render(request, "core/news.html", {"news": news_})


def login_view(request):
    if request.method == "POST":
        try:
            number_token = NumberToken.objects.get(
                number_token=request.POST["number_token"]
            )

        except:
            messages.error(
                request, "Bunday kodni topa olmadik, qaytadan sinab ko'ring!"
            )
            return redirect("core:login")

        if not number_token.is_expired():
            if request.user.is_authenticated:
                logout(request)
            login(request, user=number_token.user)
            message = random.choice(
                [
                    "Bugun qaysi joyda o'tiramiz",
                    "Sumkamizni tayyorladikmi, kitoblarni oldikmi?",
                    "Yozda kun issiq, nima qilibdi Ijod Saroyda konditsionerlar ishlaydi-ku",
                ]
            )
            messages.success(
                request, f"Assalomu {request.user.people.name}, Xush kelibsiz!"
            )
            messages.info(request, message)
            number_token.delete()
            return redirect("core:home")
        else:
            number_token.delete()
            messages.error(
                request, "Bu kod allaqachon eskirgan qayta olib sinab ko'ring"
            )
            return redirect("core:login")

    return render(request, "core/auth/login.html")


@login_required(login_url="core:login")
def booking(request):
    return render(request, "core/booking.html")
