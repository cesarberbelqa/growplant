from django.db import models
from django.contrib.auth.models import User

class Environment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dimensions = models.CharField(max_length=50, blank=True)
    lighting_type = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.dimensions


class Cultivation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.environment.dimensions

class Plant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cultivation = models.ForeignKey(Cultivation, on_delete=models.CASCADE)
    environment = models.OneToOneField(Environment, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100, blank=True)
    variety = models.CharField(max_length=100, blank=True)
    planting_date = models.DateTimeField()
    growth_stage = models.CharField(max_length=50, choices=[
        ('seed', 'Seed'),
        ('seedling', 'Seedling'),
        ('vegetative', 'Vegetative'),
        ('flowering', 'Flowering'),
        ('harvest', 'Harvest')
    ], blank=True)
    notes = models.TextField(blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    trunk_diameter = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

class Fertilizer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    fertilizer_type = models.CharField(max_length=100)
    fertilizer_brand = models.CharField(max_length=100)

class EnvironmentRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cultivation = models.ForeignKey(Cultivation, on_delete=models.CASCADE)
    environment = models.OneToOneField(Environment, on_delete=models.CASCADE)
    date = models.DateTimeField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    ventilation_system = models.CharField(max_length=100)
    co2_level = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    light_intensity = models.IntegerField(null=True, blank=True)

class ImageRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='Cultivation/imagens')

class WateringRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    watering_date = models.DateTimeField()
    water_amount = models.DecimalField(max_digits=5, decimal_places=2)
    water_ph = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    water_ppm = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    watering_method = models.CharField(max_length=50, choices=[
        ('manual', 'Manual'),
        ('automatic', 'Automatic')
    ])

class FertilizerRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wateringrecord = models.ForeignKey(WateringRecord, on_delete=models.CASCADE)
    dosage = models.DecimalField(max_digits=5, decimal_places=2)

class PestDisease(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    identification_date = models.DateTimeField()
    type = models.CharField(max_length=100, blank=True)
    treatment = models.TextField(blank=True)
    image = models.ImageField(upload_to='cultivos/imagens', blank=True)
