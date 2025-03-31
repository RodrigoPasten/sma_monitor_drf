from django.db import models

# Create your models here.
class Organismo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    sigla = models.CharField(max_length=20, unique=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre