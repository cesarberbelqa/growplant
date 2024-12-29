from django.contrib import admin

from .models import Environment, VentilationType, HumidityControlType, LightType

# ...
admin.site.register(Environment)
admin.site.register(VentilationType)
admin.site.register(HumidityControlType)
admin.site.register(LightType)
