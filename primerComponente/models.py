from venv import create
from django.db import models
from django.utils import timezone

# Create your models here.
class PrimerTabla(models.Model):
    nombre = models.CharField(max_length = 50, null = False)
    edad = models.IntegerField(default = 0)
    create = models.DateTimeField(default=timezone.now)
    edir = models.DateTimeField(blank=True, null=True, default=None)
