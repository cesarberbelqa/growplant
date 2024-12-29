from django.db import models

from grow.base import BaseClass
from grow.models import Cultivation

class VentilationType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class HumidityControlType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class LightType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Light(models.Model):
    name = models.CharField(max_length=50)
    wattage = models.FloatField()  # Potência da luz em watts
    type = models.ForeignKey(LightType, on_delete=models.CASCADE)
    environment = models.ForeignKey('Environment', on_delete=models.CASCADE, related_name='lights')

    def __str__(self):
        return f"{self.name} ({self.wattage}W, {self.type})"

class Ventilation(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(VentilationType, on_delete=models.CASCADE)
    has_filter = models.BooleanField(default=False, help_text="Applicable for exhaust ventilation only")
    environment = models.ForeignKey('Environment', on_delete=models.CASCADE, related_name='ventilations')

    def __str__(self):
        filter_info = "with filter" if self.has_filter else "no filter"
        return f"{self.name} ({self.type}) {filter_info}"

class HumidityControl(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(HumidityControlType, on_delete=models.CASCADE)
    environment = models.ForeignKey('Environment', on_delete=models.CASCADE, related_name='humidity_controls')

    def __str__(self):
        return f"{self.name} ({self.type})"

class TemperatureControl(models.Model):
    name = models.CharField(max_length=50)
    wattage = models.FloatField(help_text="Power of the heater in watts")
    environment = models.ForeignKey('Environment', on_delete=models.CASCADE, related_name='temperature_controls')

    def __str__(self):
        return f"{self.name} ({self.wattage}W)"

class Pot(models.Model):
    name = models.CharField(max_length=50)
    volume = models.FloatField(help_text="Volume in liters")
    environment = models.ForeignKey('Environment', on_delete=models.CASCADE, related_name='pots')

    def __str__(self):
        return f"{self.name} ({self.volume}L)"

class Tent(models.Model):
    name = models.CharField(max_length=50)
    height = models.IntegerField(help_text="Height in cm")
    width = models.IntegerField(help_text="Width in cm")
    length = models.IntegerField(help_text="Length in cm")
    environment = models.OneToOneField('Environment', on_delete=models.CASCADE, related_name='tent')

    def __str__(self):
        return f"{self.name} ({self.height}x{self.width}x{self.length} cm)"

class Environment(models.Model):
    cultivation = models.ForeignKey(Cultivation, on_delete=models.CASCADE, related_name='cultivations')
    name = models.CharField(max_length=50)
    

    def __str__(self):
        return f"Environment: {self.name}"