import datetime
import uuid

from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
import qrcode

from .functions import generate_numbers


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]


class NewsManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(status=True)


class Room(BaseModel):
    class Floors(models.IntegerChoices):
        MINUS_ONE = -1, "-1-qavat"
        FIRST = 1, "1-qavat"
        SECOND = 2, "2-qavat"

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to="images/rooms/")
    description = models.TextField()
    floor = models.IntegerField(choices=Floors.choices, null=True, blank=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Room, self).save(*args, **kwargs)


class News(BaseModel):
    objects = models.Manager()
    published = NewsManager()

    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True)
    image = models.ImageField(upload_to="images/news/")
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    views = models.IntegerField(default=0)
    is_event = models.BooleanField(default=False)
    # room = models.ForeignKey(
    #     Room,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     related_name='news'
    # ) core.News.room: (models.E006) The field 'room' clashes with the field 'room' from model 'core.basemodel'.
    status = models.BooleanField(default=False)

    description = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)

    def update_views(self):
        self.views += 1
        self.save()
        return self.views


class MessageFromGuestUser(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class NumberToken(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name="number_token",
        blank=True,
    )
    people = models.OneToOneField(
        "People", on_delete=models.CASCADE, null=True, related_name="number_token"
    )
    number_token = models.CharField(max_length=6, default=generate_numbers, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.number_token

    def save(self, *args, **kwargs):
        self.user = self.people.user
        super(NumberToken, self).save(*args, **kwargs)

    def is_expired(self):
        return timezone.now() > self.updated_at + datetime.timedelta(minutes=1)

    def check_token(self, number_token):
        if self.is_expired():
            return False

        return self.number_token == number_token

    def update_token(self):
        self.number_token = generate_numbers()
        self.save()
        return self.number_token


# Kreativ Park previous models


class Seat(BaseModel):
    ID = models.CharField(max_length=20, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    has_taken = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to="images/seats/", default="images/no_image.png", blank=True
    )

    def __str__(self):
        return self.name


class People(models.Model):
    ID = models.CharField(max_length=40, primary_key=True, unique=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="people", null=True, blank=True
    )
    name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    passport_data = models.CharField(max_length=50, blank=True, null=True)
    birthday_date = models.DateField(null=True, blank=True)
    image = models.ImageField(
        upload_to="images/people/", default="images/people/default_user.jpg", blank=True
    )
    seat = models.OneToOneField(
        Seat, on_delete=models.CASCADE, related_name="people", null=True, blank=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.name:
            user = User.objects.create_user(username=self.ID, password=self.ID)
            self.user = user
        super(People, self).save(*args, **kwargs)


class QrCode(models.Model):
    class Types(models.TextChoices):
        IN = "IN", "Kirish"
        OUT = "OUT", "Chiqish"

    ID = models.CharField(
        primary_key=True, default=uuid.uuid4, unique=True, max_length=40
    )
    people = models.OneToOneField(
        People, on_delete=models.CASCADE, related_name="qrcode"
    )
    image_path = models.CharField(max_length=1024)
    type = models.CharField(max_length=3, choices=Types.choices)
    purpose = models.CharField(max_length=1024, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_at} - {self.people.name}"

    def create_qr_code(self):
        qrcode_img = qrcode.make(self.ID)
        qrcode_img.save(f"media/images/qrcodes/{self.ID}.png")
        self.image_path = f"images/qrcodes/{self.ID}.png"
        self.save()
        return self.image_path


class Data(models.Model):
    class Types(models.TextChoices):
        IN = "IN", "Kirish"
        OUT = "OUT", "Chiqish"

    people = models.ForeignKey(People, on_delete=models.CASCADE, related_name="data")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    purpose = models.CharField(max_length=1024)
    type = models.CharField(max_length=3, choices=Types.choices)

    def __str__(self):
        return f"{self.people.name} - {self.purpose} - {self.created_at}"
