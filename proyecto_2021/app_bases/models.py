from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class ClaseModelo(models.Model):

    estado = models.BooleanField(default=True)

    fc = models.DateTimeField(auto_now_add=True)

    fm = models.DateTimeField(auto_now=True)

    uc = models.ForeignKey(User, on_delete=models.CASCADE)

    um = models.IntegerField(blank=True, null=True)

    # No a producción

    class Meta:
        abstract = True
