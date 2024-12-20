# Generated by Django 5.1.4 on 2024-12-19 21:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Environment",
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
                ("dimensions", models.CharField(blank=True, max_length=50)),
                ("lighting_type", models.CharField(blank=True, max_length=50)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cultivation",
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
                ("start_date", models.DateTimeField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "environment",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="grow.environment",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EnvironmentRecord",
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
                ("date", models.DateTimeField()),
                ("temperature", models.DecimalField(decimal_places=2, max_digits=5)),
                ("humidity", models.DecimalField(decimal_places=2, max_digits=5)),
                ("ventilation_system", models.CharField(max_length=100)),
                (
                    "co2_level",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("light_intensity", models.IntegerField(blank=True, null=True)),
                (
                    "cultivation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="grow.cultivation",
                    ),
                ),
                (
                    "environment",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="grow.environment",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Fertilizer",
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
                ("name", models.CharField(max_length=100)),
                ("fertilizer_type", models.CharField(max_length=100)),
                ("fertilizer_brand", models.CharField(max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Plant",
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
                ("name", models.CharField(max_length=100)),
                ("species", models.CharField(blank=True, max_length=100)),
                ("variety", models.CharField(blank=True, max_length=100)),
                ("planting_date", models.DateTimeField()),
                (
                    "growth_stage",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("seed", "Seed"),
                            ("seedling", "Seedling"),
                            ("vegetative", "Vegetative"),
                            ("flowering", "Flowering"),
                            ("harvest", "Harvest"),
                        ],
                        max_length=50,
                    ),
                ),
                ("notes", models.TextField(blank=True)),
                (
                    "height",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "trunk_diameter",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "cultivation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="grow.cultivation",
                    ),
                ),
                (
                    "environment",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="grow.environment",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PestDisease",
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
                ("identification_date", models.DateTimeField()),
                ("type", models.CharField(blank=True, max_length=100)),
                ("treatment", models.TextField(blank=True)),
                ("image", models.ImageField(blank=True, upload_to="cultivos/imagens")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "plant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="grow.plant"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ImageRecord",
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
                ("date", models.DateTimeField()),
                ("image", models.ImageField(upload_to="Cultivation/imagens")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "plant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="grow.plant"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WateringRecord",
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
                ("watering_date", models.DateTimeField()),
                ("water_amount", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "water_ph",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=5),
                ),
                (
                    "water_ppm",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=5),
                ),
                (
                    "watering_method",
                    models.CharField(
                        choices=[("manual", "Manual"), ("automatic", "Automatic")],
                        max_length=50,
                    ),
                ),
                (
                    "plant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="grow.plant"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FertilizerRecord",
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
                ("dosage", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "wateringrecord",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="grow.wateringrecord",
                    ),
                ),
            ],
        ),
    ]