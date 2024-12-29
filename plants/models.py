from django.db import models
from django.utils.timezone import now
from envs.models import Environment
from grow.base import BaseClass

# Create your models here.
class Plant(BaseClass):
    environment = models.OneToOneField(Environment, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100, blank=True)
    variety = models.CharField(max_length=100, blank=True)
    planting_date = models.DateTimeField(default=now)
    growth_stage = models.CharField(max_length=50, choices=[
        ('seed', 'Seed'),
        ('seedling', 'Seedling'),
        ('vegetative', 'Vegetative'),
        ('flowering', 'Flowering'),
        ('harvest', 'Harvest')
    ], blank=True)
    notes = models.TextField(blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name + ' / ' + self.species + ' / ' + self.variety