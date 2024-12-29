from django import forms
from .models import Cultivation

class CultivationForm(forms.ModelForm):
    class Meta:
        model = Cultivation
        exclude = ['user', 'created_at', 'updated_at']