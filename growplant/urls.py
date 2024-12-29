
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("accounts.urls")),
    path("cultivations/", include("grow.urls")),
    path("environments/", include("envs.urls")),
    path("plants/", include("plants.urls")),
    path("admin/", admin.site.urls),
]