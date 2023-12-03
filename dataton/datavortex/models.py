from django.db import models

# Create your models here.
# models.py

from django.db import models


class DashboardItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
