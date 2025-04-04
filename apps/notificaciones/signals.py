# apps/notificaciones/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.usuarios.models import Usuario
from .models import ConfiguracionNotificaciones, TipoNotificacion


@receiver(post_save, sender=Usuario)
def crear_configuracion_notificaciones(sender, instance, created, **kwargs):
    """
    Crea una configuración de notificaciones para cada usuario nuevo.
    """
    if created:
        # Crear configuración básica
        config = ConfiguracionNotificaciones.objects.create(
            usuario=instance,
            recibir_email=instance.recibir_notificaciones_email,
            recibir_sistema=instance.recibir_notificaciones_sistema
        )

        # Añadir todos los tipos de notificación relevantes según el rol del usuario
        tipos_relevantes = []

        if instance.is_superadmin:
            tipos_relevantes.extend(TipoNotificacion.objects.filter(para_superadmin=True))
        elif instance.is_admin_sma:
            tipos_relevantes.extend(TipoNotificacion.objects.filter(para_admin_sma=True))
        elif instance.is_organismo:
            tipos_relevantes.extend(TipoNotificacion.objects.filter(para_organismos=True))
        elif instance.is_ciudadano:
            tipos_relevantes.extend(TipoNotificacion.objects.filter(para_ciudadanos=True))

        # Añadir los tipos encontrados a la configuración
        config.tipos_habilitados.add(*tipos_relevantes)