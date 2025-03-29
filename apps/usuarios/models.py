from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ORGANISMOS = [
        ('municipalidad', 'Municipalidad'),
        ('carabineros', 'Carabineros'),
        ('corfo', 'CORFO'),
    ]

    ROLES = [
        ('admin', 'Administrador'),
        ('editor', 'Editor'),
        ('viewer', 'Visualizador'),
    ]

    organismo = models.CharField(max_length=50, choices=ORGANISMOS)
    rol = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return f"{self.username} - {self.organismo} - {self.rol}"
