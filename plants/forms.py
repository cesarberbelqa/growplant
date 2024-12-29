from django import forms
from .models import Plant

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        exclude = ['user', 'created_at', 'updated_at']