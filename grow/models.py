from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

from grow.base import BaseClass


class Cultivation(BaseClass):
    name = models.CharField(max_length=20)
    start_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.name 

# class Fertilizer(BaseClass):
#     name = models.CharField(max_length=100)
#     fertilizer_type = models.CharField(max_length=100)
#     fertilizer_brand = models.CharField(max_length=100)

# class EnvironmentRecord(BaseClass):
#     cultivation = models.ForeignKey(Cultivation, on_delete=models.CASCADE)
#     environment = models.OneToOneField(Environment, on_delete=models.CASCADE)
#     temperature = models.DecimalField(max_digits=5, decimal_places=2)
#     humidity = models.DecimalField(max_digits=5, decimal_places=2)
#     ventilation_system = models.CharField(max_length=100)
#     co2_level = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
#     light_intensity = models.IntegerField(null=True, blank=True)

# class ImageRecord(BaseClass):
#     plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='Cultivation/imagens')

# class WateringRecord(BaseClass):
#     plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
#     watering_date = models.DateTimeField()
#     water_amount = models.DecimalField(max_digits=5, decimal_places=2)
#     water_ph = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
#     water_ppm = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
#     watering_method = models.CharField(max_length=50, choices=[
#         ('manual', 'Manual'),
#         ('automatic', 'Automatic')
#     ])

# class FertilizerRecord(BaseClass):
#     wateringrecord = models.ForeignKey(WateringRecord, on_delete=models.CASCADE)
#     dosage = models.DecimalField(max_digits=5, decimal_places=2)

# class PestDisease(BaseClass):
#     plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
#     identification_date = models.DateTimeField()
#     type = models.CharField(max_length=100, blank=True)
#     treatment = models.TextField(blank=True)
#     image = models.ImageField(upload_to='cultivos/imagens', blank=True)
