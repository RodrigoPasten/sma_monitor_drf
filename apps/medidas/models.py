from django.db import models
from apps.usuarios.models import Usuario

# Create your models here.
class Medida(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=255)
    
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def delete(self, *args, **kwargs):
        """This override delete method to just change state of activo field"""
        self.activo = False
        self.save()
    
    def __str__(self):
        return f"{self.nombre} - {self.descripcion}"
    
class LogMedida(models.Model):
    ACCIONES = [
        ('crear', 'Crear'),
        ('actualizar', 'Actualizar'),
        ('eliminar', 'Eliminar'),
    ]
    
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    medida = models.ForeignKey(Medida, on_delete=models.CASCADE)
    accion = models.CharField(max_length=20, choices=ACCIONES)
    fecha=models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self):
        return f"{self.usuario.username} - {self.medida.nombre} - {self.accion} - {self.fecha}"