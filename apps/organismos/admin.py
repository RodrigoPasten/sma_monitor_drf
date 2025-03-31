from django.contrib import admin
from .models import Organismo

# Register your models here.
@admin.register(Organismo)
class OrganismoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'sigla')
    search_fields = ('nombre', 'sigla')
    list_filter = ('activo',)