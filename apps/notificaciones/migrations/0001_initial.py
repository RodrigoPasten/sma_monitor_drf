# Generated by Django 5.1.7 on 2025-04-04 21:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medidas', '0002_componente_alter_logmedida_options_and_more'),
        ('organismos', '0003_tipoorganismo_alter_organismo_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoNotificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('codigo', models.CharField(max_length=50, unique=True, verbose_name='Código')),
                ('icono', models.CharField(blank=True, max_length=50, verbose_name='Icono')),
                ('color', models.CharField(blank=True, help_text='Código hexadecimal del color, ej: #FF5733', max_length=7, verbose_name='Color')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
                ('para_superadmin', models.BooleanField(default=False, verbose_name='Para Super Admin')),
                ('para_admin_sma', models.BooleanField(default=False, verbose_name='Para Admin SMA')),
                ('para_organismos', models.BooleanField(default=False, verbose_name='Para Organismos')),
                ('para_ciudadanos', models.BooleanField(default=False, verbose_name='Para Ciudadanos')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Tipo de Notificación',
                'verbose_name_plural': 'Tipos de Notificaciones',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Recordatorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('fecha_programada', models.DateTimeField(verbose_name='Fecha programada')),
                ('fecha_enviado', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de envío')),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('enviado', 'Enviado'), ('cancelado', 'Cancelado')], default='pendiente', max_length=20, verbose_name='Estado')),
                ('repeticion', models.CharField(choices=[('ninguna', 'No repetir'), ('diaria', 'Diariamente'), ('semanal', 'Semanalmente'), ('mensual', 'Mensualmente'), ('anual', 'Anualmente')], default='ninguna', max_length=20, verbose_name='Repetición')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recordatorios_creados', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('medida', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recordatorios', to='medidas.medida', verbose_name='Medida')),
                ('organismo', models.ForeignKey(blank=True, help_text='Si se especifica, el recordatorio se enviará a todos los usuarios de este organismo', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recordatorios', to='organismos.organismo', verbose_name='Organismo')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recordatorios', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Recordatorio',
                'verbose_name_plural': 'Recordatorios',
                'ordering': ['fecha_programada'],
            },
        ),
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
                ('enlace', models.CharField(blank=True, help_text='URL a la que dirigir al usuario al hacer clic en la notificación', max_length=255, verbose_name='Enlace')),
                ('fecha_envio', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de envío')),
                ('leida', models.BooleanField(default=False, verbose_name='Leída')),
                ('fecha_lectura', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de lectura')),
                ('enviada_email', models.BooleanField(default=False, verbose_name='Enviada por email')),
                ('fecha_envio_email', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de envío por email')),
                ('medida', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notificaciones', to='medidas.medida', verbose_name='Medida')),
                ('organismo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notificaciones', to='organismos.organismo', verbose_name='Organismo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones', to='notificaciones.tiponotificacion', verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Notificación',
                'verbose_name_plural': 'Notificaciones',
                'ordering': ['-fecha_envio'],
            },
        ),
        migrations.CreateModel(
            name='ConfiguracionNotificaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recibir_email', models.BooleanField(default=True, verbose_name='Recibir por email')),
                ('recibir_sistema', models.BooleanField(default=True, verbose_name='Recibir en el sistema')),
                ('frecuencia_email', models.CharField(choices=[('inmediata', 'Inmediata'), ('diaria', 'Resumen diario'), ('semanal', 'Resumen semanal')], default='inmediata', max_length=20, verbose_name='Frecuencia de emails')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='configuracion_notificaciones', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
                ('tipos_habilitados', models.ManyToManyField(help_text='Tipos de notificaciones que el usuario desea recibir', related_name='configuraciones', to='notificaciones.tiponotificacion', verbose_name='Tipos habilitados')),
            ],
            options={
                'verbose_name': 'Configuración de Notificaciones',
                'verbose_name_plural': 'Configuraciones de Notificaciones',
            },
        ),
    ]
