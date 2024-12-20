from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('password_reset/', views.password_reset_request, name='password_reset'),

    path('environments/', views.environment_list, name='environment_list'),
    path('environments/<int:pk>/', views.environment_detail, name='environment_detail'),
    path('environments/new/', views.environment_create, name='environment_create'),
    path('environments/<int:pk>/edit/', views.environment_update, name='environment_update'),
    path('environments/<int:pk>/delete/', views.environment_delete, name='environment_delete'),

    path('plants/', views.plant_list, name='plant_list'),
    path('plants/<int:pk>/', views.plant_detail, name='plant_detail'),
    path('plants/new/', views.plant_create, name='plant_create'),
    path('plants/<int:pk>/edit/', views.plant_update, name='plant_update'),
    path('plants/<int:pk>/delete/', views.plant_delete, name='plant_delete'),

    path('cultivations/', views.cultivation_list, name='cultivation_list'),
    path('cultivations/<int:pk>/', views.cultivation_detail, name='cultivation_detail'),
    path('cultivations/new/', views.cultivation_create, name='cultivation_create'),
    path('cultivations/<int:pk>/edit/', views.cultivation_update, name='cultivation_update'),
    path('cultivations/<int:pk>/delete/', views.cultivation_delete, name='cultivation_delete'),
]