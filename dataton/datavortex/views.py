# views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import DashboardItem


def get_dashboard_data(request):
    items = DashboardItem.objects.all()
    data = [{"title": item.title, "description": item.description} for item in items]
    return JsonResponse({"data": data})
