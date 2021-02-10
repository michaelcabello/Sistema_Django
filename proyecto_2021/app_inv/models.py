from django.db import models

from app_bases.models import ClaseModelo

# Create your models here.

class Categoria(ClaseModelo):

    descripcion = models.CharField(
        
        max_length=100,

        help_text = 'Descripción del maiki',

        unique = True

    )

    # Falta comprender

    def __str__(self):
        return f'{self.descripcion}'

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural = 'Categorias'
