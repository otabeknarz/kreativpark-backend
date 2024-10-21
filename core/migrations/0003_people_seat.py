# Generated by Django 5.0.6 on 2024-07-16 03:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_remove_people_seat"),
    ]

    operations = [
        migrations.AddField(
            model_name="people",
            name="seat",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="people",
                to="core.seat",
            ),
        ),
    ]
