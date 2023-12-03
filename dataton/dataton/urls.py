from django.urls import path
from django.contrib import admin
from datavortex.views import get_dashboard_data

urlpatterns = [
    # admin
    path("admin", admin.site.urls),
    path("api/dashboard/", get_dashboard_data, name="dashboard_data"),
    # Agrega otras URLs según sea necesario
]
