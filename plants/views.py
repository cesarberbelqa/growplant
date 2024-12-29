from django.shortcuts import redirect, render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from plants.forms import PlantForm
from plants.models import Plant

#
# PLANT
#
@login_required(login_url='home')
def plant_list(request):
    if request.method == 'POST':
        form = PlantForm(request.POST)
        if form.is_valid():
            plant = form.save(commit=False)
            plant.user = request.user
            plant.save()            
    
    form = PlantForm()
    plants = Plant.objects.filter(user=request.user)
    return render(request, 'plant_list.html', {'form': form,'plants': plants})

@login_required(login_url='home')
def plant_delete(request, pk):
    plant = get_object_or_404(Plant, pk=pk, user=request.user)
    if request.method == "POST":
        plant.delete()
    return redirect('plant_list')

@login_required(login_url='home')
def plant_update(request, pk):
    plant = get_object_or_404(Plant, pk=pk, user=request.user)
    if request.method == "POST":
        form = PlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plant_list')
    else:
        form = PlantForm(instance=plant)
    # Configurando o queryset do campo environment
    plants = Plant.objects.filter(user=request.user)
    return render(request, 'plant_list.html', {'form': form,'plants': plants})