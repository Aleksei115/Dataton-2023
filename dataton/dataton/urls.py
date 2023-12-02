# urls.py

from django.urls import path
from datavortex.views import get_dashboard_data

urlpatterns = [
    path("api/dashboard/", get_dashboard_data, name="dashboard_data"),
    # Agrega otras URLs según sea necesario
]
