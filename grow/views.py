from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Cultivation
from .forms import CultivationForm
from envs.models import Environment
#
# CULTIVATION
#
@login_required(login_url='home')
def cultivation_list(request):
    if request.method == 'POST':
        form = CultivationForm(request.POST)
        if form.is_valid():
            cultivation = form.save(commit=False)
            cultivation.user = request.user
            cultivation.save()            
    
    form = CultivationForm()
    cultivations = Cultivation.objects.filter(user=request.user)
    # envs = Environment.objects.filter(user=request.user)
    # print(envs.count())
    # if envs.count() == 0:
    #     return redirect('environment_list')
    # form.fields['environment'].queryset = envs
    return render(request, 'cultivation_list.html', {'form': form,'cultivations': cultivations})

@login_required(login_url='home')
def cultivation_delete(request, pk):
    cultivation = get_object_or_404(Cultivation, pk=pk, user=request.user)
    if request.method == "POST":
        cultivation.delete()
    return redirect('cultivation_list')

@login_required(login_url='home')
def cultivation_update(request, pk):
    cultivation = get_object_or_404(Cultivation, pk=pk, user=request.user)
    if request.method == "POST":
        form = CultivationForm(request.POST, instance=cultivation)
        if form.is_valid():
            form.save()
            return redirect('cultivation_list')
    else:
        form = CultivationForm(instance=cultivation)
    # Configurando o queryset do campo environment
    envs = Environment.objects.filter(user=request.user)
    form.fields['environment'].queryset = envs
    cultivations = Cultivation.objects.filter(user=request.user)
    return render(request, 'cultivation_list.html', {'form': form,'cultivations': cultivations})