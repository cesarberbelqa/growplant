from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Plant, Cultivation, Environment
from .forms import PlantForm, CultivationForm, EnvironmentForm

def home(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('cultivation_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(from_email=settings.DEFAULT_FROM_EMAIL, request=request)
            return redirect('home')
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset.html', {'form': form})

@login_required
def user_cultivation_list(request):
    cultivations = Cultivation.objects.filter(user=request.user)
    return render(request, 'user_cultivation_list.html', {'cultivations': cultivations})

@login_required
def environment_list(request):
    environments = Environment.objects.filter(user=request.user)
    return render(request, 'environment_list.html', {'environments': environments})

@login_required
def environment_detail(request, pk):
    environment = get_object_or_404(Environment, pk=pk, user=request.user)
    return render(request, 'environment_detail.html', {'environment': environment})

@login_required
def environment_create(request):
    if request.method == "POST":
        form = EnvironmentForm(request.POST)
        if form.is_valid():
            environment = form.save(commit=False)
            environment.user = request.user
            environment.save()
            return redirect('environment_list')
    else:
        form = EnvironmentForm()
    return render(request, 'environment_form.html', {'form': form})

@login_required
def environment_update(request, pk):
    environment = get_object_or_404(Environment, pk=pk, user=request.user)
    if request.method == "POST":
        form = EnvironmentForm(request.POST, instance=environment)
        if form.is_valid():
            form.save()
            return redirect('environment_list')
    else:
        form = EnvironmentForm(instance=environment)
    return render(request, 'environment_form.html', {'form': form})

@login_required
def environment_delete(request, pk):
    environment = get_object_or_404(Environment, pk=pk, user=request.user)
    if request.method == "POST":
        environment.delete()
        return redirect('environment_list')
    return render(request, 'environment_confirm_delete.html', {'environment': environment})

@login_required
def plant_list(request):
    plants = Plant.objects.filter(user=request.user)
    return render(request, 'plant_list.html', {'plants': plants})

@login_required
def plant_detail(request, pk):
    plant = get_object_or_404(Plant, pk=pk, user=request.user)
    return render(request, 'plant_detail.html', {'plant': plant})

@login_required
def plant_create(request):
    if request.method == "POST":
        form = PlantForm(request.POST)
        if form.is_valid():
            plant = form.save(commit=False)
            plant.user = request.user
            plant.save()
            return redirect('plant_list')
    else:
        form = PlantForm()
        # Filtrar os registros pelo usuário logado
        form.fields['cultivation'].queryset = Cultivation.objects.filter(user=request.user)
        form.fields['environment'].queryset = Environment.objects.filter(user=request.user)
    return render(request, 'plant_form.html', {'form': form, 'title': 'Create Plant'})

@login_required
def plant_update(request, pk):
    plant = get_object_or_404(Plant, pk=pk, user=request.user)
    if request.method == "POST":
        form = PlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plant_list')
    else:
        form = PlantForm(instance=plant)
        # Filtrar os registros pelo usuário logado
        form.fields['cultivation'].queryset = Cultivation.objects.filter(user=request.user)
        form.fields['environment'].queryset = Environment.objects.filter(user=request.user)
    return render(request, 'plant_form.html', {'form': form, 'title': 'Edit Plant'})


@login_required
def plant_delete(request, pk):
    plant = get_object_or_404(Plant, pk=pk, user=request.user)
    if request.method == "POST":
        plant.delete()
        return redirect('plant_list')
    return render(request, 'plant_confirm_delete.html', {'plant': plant})

@login_required
def cultivation_list(request):
    cultivations = Cultivation.objects.filter(user=request.user)
    return render(request, 'cultivation_list.html', {'cultivations': cultivations})

@login_required
def cultivation_detail(request, pk):
    cultivation = get_object_or_404(Cultivation, pk=pk, user=request.user)
    return render(request, 'cultivation_detail.html', {'cultivation': cultivation})

@login_required
def cultivation_create(request):
    if request.method == "POST":
        form = CultivationForm(request.POST)
        if form.is_valid():
            cultivation = form.save(commit=False)
            cultivation.user = request.user
            cultivation.save()
            return redirect('cultivation_list')
    else:
        form = CultivationForm()
    # Configurando o queryset do campo environment
    form.fields['environment'].queryset = Environment.objects.filter(user=request.user)
    return render(request, 'cultivation_form.html', {'form': form, 'title': 'Create Cultivation'})


@login_required
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
    form.fields['environment'].queryset = Environment.objects.filter(user=request.user)
    return render(request, 'cultivation_form.html', {'form': form, 'title': 'Edit Cultivation'})

@login_required
def cultivation_delete(request, pk):
    cultivation = get_object_or_404(Cultivation, pk=pk, user=request.user)
    if request.method == "POST":
        cultivation.delete()
        return redirect('cultivation_list')
    return render(request, 'cultivation_confirm_delete.html', {'cultivation': cultivation})
