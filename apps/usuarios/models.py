from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.organismos.models import Organismo

class Usuario(AbstractUser):
    """ ORGANISMOS = [
        ('municipalidad', 'Municipalidad'),
        ('carabineros', 'Carabineros'),
        ('corfo', 'CORFO'),
    ] """

    ROLES = [
        ('admin', 'Administrador'),
        ('editor', 'Editor'),
        ('viewer', 'Visualizador'),
    ]

    organismo = models.ForeignKey(Organismo, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=ROLES)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} - {self.organismo.nombre} - {self.rol}"
