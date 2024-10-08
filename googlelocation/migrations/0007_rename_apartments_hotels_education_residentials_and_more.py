# Generated by Django 5.1.1 on 2024-10-07 08:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("googlelocation", "0006_apartments_source_location_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Apartments",
            new_name="Hotels",
        ),
        migrations.CreateModel(
            name="Education",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("status", models.CharField(default="default", max_length=25)),
                ("address", models.CharField(max_length=300)),
                ("coordinates", models.TextField(max_length=300)),
                ("types", models.TextField(max_length=500)),
                ("rating", models.CharField(max_length=10)),
                ("user_rating", models.CharField(max_length=10)),
                ("Travel_Distance", models.CharField(max_length=10)),
                ("Travel_Time", models.CharField(max_length=10)),
                (
                    "source_location",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="googlelocation.sourcelocation",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Residentials",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("status", models.CharField(default="default", max_length=25)),
                ("address", models.CharField(max_length=300)),
                ("coordinates", models.TextField(max_length=300)),
                ("types", models.TextField(max_length=500)),
                ("rating", models.CharField(max_length=10)),
                ("user_rating", models.CharField(max_length=10)),
                ("Travel_Distance", models.CharField(max_length=10)),
                ("Travel_Time", models.CharField(max_length=10)),
                (
                    "source_location",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="googlelocation.sourcelocation",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Toursit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("status", models.CharField(default="default", max_length=25)),
                ("address", models.CharField(max_length=300)),
                ("coordinates", models.TextField(max_length=300)),
                ("types", models.TextField(max_length=500)),
                ("rating", models.CharField(max_length=10)),
                ("user_rating", models.CharField(max_length=10)),
                ("Travel_Distance", models.CharField(max_length=10)),
                ("Travel_Time", models.CharField(max_length=10)),
                (
                    "source_location",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="googlelocation.sourcelocation",
                    ),
                ),
            ],
        ),
    ]
