from django import forms
from django.forms import inlineformset_factory
from .models import Environment, Tent, Light, Ventilation, HumidityControl, TemperatureControl, Pot

# Forms
class EnvironmentForm(forms.ModelForm):
    class Meta:
        model = Environment
        fields = ['name', 'cultivation']
        # exclude = ['user', 'created_at', 'updated_at']

class TentForm(forms.ModelForm):
    class Meta:
        model = Tent
        fields = ['name', 'height', 'width', 'length']
        exclude = ['user', 'created_at', 'updated_at']

LightFormSet = inlineformset_factory(Environment, Light, fields=['name', 'wattage', 'type'], extra=1, can_delete=True)
VentilationFormSet = inlineformset_factory(Environment, Ventilation, fields=['name', 'type', 'has_filter'], extra=1, can_delete=True)
HumidityControlFormSet = inlineformset_factory(Environment, HumidityControl, fields=['name', 'type'], extra=1, can_delete=True)
TemperatureControlFormSet = inlineformset_factory(Environment, TemperatureControl, fields=['name', 'wattage'], extra=1, can_delete=True)
PotFormSet = inlineformset_factory(Environment, Pot, fields=['name', 'volume'], extra=1, can_delete=True)