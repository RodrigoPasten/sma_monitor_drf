from django.contrib import admin
from .models import Medida

# Register your models here.
@admin.register(Medida)
class MedidaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)
    list_filter = ('activo',)