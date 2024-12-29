from django import forms
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.views import View

from envs.forms import EnvironmentForm, TentForm, LightFormSet, VentilationFormSet, HumidityControlFormSet, TemperatureControlFormSet, PotFormSet
from .models import Environment
from grow.models import Cultivation

def environment_list(request,pk=None):
    template_name = 'environment_list.html'
    cultivations = Cultivation.objects.filter(user=request.user)
    print(cultivations.count())
    if request.method == 'GET':
        environment = Environment.objects.get(pk=pk) if pk else None
        environment_form = EnvironmentForm(instance=environment, initial={'cultivation': cultivations})
        tent_form = TentForm(instance=environment.tent if environment and hasattr(environment, 'tent') else None)
        light_formset = LightFormSet(instance=environment)
        ventilation_formset = VentilationFormSet(instance=environment)
        humidity_control_formset = HumidityControlFormSet(instance=environment)
        temperature_control_formset = TemperatureControlFormSet(instance=environment)
        pot_formset = PotFormSet(instance=environment)

        context = {
            'environment_form': environment_form,
            'tent_form': tent_form,
            'light_formset': light_formset,
            'ventilation_formset': ventilation_formset,
            'humidity_control_formset': humidity_control_formset,
            'temperature_control_formset': temperature_control_formset,
            'pot_formset': pot_formset,
        }
        return render(request, template_name, context)

    else:
        environment = Environment.objects.get(pk=pk) if pk else None
        environment_form = EnvironmentForm(request.POST, instance=environment)
        tent_form = TentForm(request.POST, instance=environment.tent if environment and hasattr(environment, 'tent') else None)
        light_formset = LightFormSet(request.POST, instance=environment)
        ventilation_formset = VentilationFormSet(request.POST, instance=environment)
        humidity_control_formset = HumidityControlFormSet(request.POST, instance=environment)
        temperature_control_formset = TemperatureControlFormSet(request.POST, instance=environment)
        pot_formset = PotFormSet(request.POST, instance=environment)

        if environment_form.is_valid() and tent_form.is_valid() and light_formset.is_valid() \
                and ventilation_formset.is_valid() and humidity_control_formset.is_valid() \
                and temperature_control_formset.is_valid() and pot_formset.is_valid():
            environment = environment_form.save()     
            environment.save()
            tent = tent_form.save(commit=False)
            tent.environment = environment
            tent.save()

            light_formset.save()
            ventilation_formset.save()
            humidity_control_formset.save()
            temperature_control_formset.save()
            pot_formset.save()

            return redirect('environment_list', pk=environment.pk)

        context = {
            'environment_form': environment_form,
            'tent_form': tent_form,
            'light_formset': light_formset,
            'ventilation_formset': ventilation_formset,
            'humidity_control_formset': humidity_control_formset,
            'temperature_control_formset': temperature_control_formset,
            'pot_formset': pot_formset,
        }
        return render(request, template_name, context)
