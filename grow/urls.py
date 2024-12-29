from django.urls import path

from . import views

urlpatterns = [
    path('', views.cultivation_list, name='cultivation_list'),
    path('<int:pk>/delete/', views.cultivation_delete, name='cultivation_delete'),
    path('<int:pk>/edit/', views.cultivation_update, name='cultivation_update'),
]