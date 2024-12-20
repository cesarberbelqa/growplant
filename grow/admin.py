from django.contrib import admin

from .models import Environment, Cultivation, Plant, Fertilizer, EnvironmentRecord, ImageRecord, WateringRecord, FertilizerRecord
# Register your models here.

admin.site.register(Environment)
admin.site.register(Cultivation)
admin.site.register(Plant)
admin.site.register(Fertilizer)
admin.site.register(EnvironmentRecord)
admin.site.register(ImageRecord)
admin.site.register(WateringRecord)
admin.site.register(FertilizerRecord)