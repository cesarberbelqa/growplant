from django.urls import path

from . import views

urlpatterns = [
    path('', views.plant_list, name='plant_list'),
    path('<int:pk>/delete/', views.plant_delete, name='plant_delete'),
    path('<int:pk>/edit/', views.plant_update, name='plant_update'),
]