# Generated by Django 5.0.7 on 2024-09-14 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_alter_people_birthday_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="seat",
            name="images",
            field=models.ImageField(blank=True, null=True, upload_to="images/seats/"),
        ),
        migrations.DeleteModel(
            name="SeatImage",
        ),
    ]