# forms.py
from django import forms
from .models import Plant, Cultivation, Environment

class EnvironmentForm(forms.ModelForm):
    class Meta:
        model = Environment
        fields = ['dimensions', 'lighting_type']
        widgets = {
            'dimensions': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter dimensions'}),
            'lighting_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter lighting type'}),
        }

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'species', 'variety', 'planting_date', 'growth_stage', 'notes', 'height', 'trunk_diameter', 'cultivation', 'environment']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter plant name'}),
            'species': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter species'}),
            'variety': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter variety'}),
            'planting_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'growth_stage': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter any notes'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter height in cm'}),
            'trunk_diameter': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter trunk diameter in cm'}),
            'cultivation': forms.Select(attrs={'class': 'form-control'}),
            'environment': forms.Select(attrs={'class': 'form-control'}),
        }

class CultivationForm(forms.ModelForm):
    class Meta:
        model = Cultivation
        fields = ['start_date', 'environment']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'environment': forms.Select(attrs={'class': 'form-control'}),
        }
