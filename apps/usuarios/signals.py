# apps/usuarios/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Usuario, Perfil

@receiver(post_save, sender=Usuario)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    """
    Crea un perfil automáticamente cuando se crea un nuevo usuario.
    """
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=Usuario)
def guardar_perfil_usuario(sender, instance, **kwargs):
    """
    Asegura que el perfil se guarde cuando se actualiza el usuario.
    """
    try:
        instance.perfil.save()
    except Perfil.DoesNotExist:
        # Si por alguna razón el perfil no existe, lo creamos
        Perfil.objects.create(usuario=instance)