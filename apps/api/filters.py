import django_filters
from apps.medidas.models import Medida, RegistroAvance
from apps.organismos.models import Organismo


class MedidaFilter(django_filters.FilterSet):
    """Filtros avanzados para el endpoint de medidas"""
    codigo_contains = django_filters.CharFilter(field_name='codigo', lookup_expr='icontains')
    nombre_contains = django_filters.CharFilter(field_name='nombre', lookup_expr='icontains')
    avance_min = django_filters.NumberFilter(field_name='porcentaje_avance', lookup_expr='gte')
    avance_max = django_filters.NumberFilter(field_name='porcentaje_avance', lookup_expr='lte')
    fecha_inicio_desde = django_filters.DateFilter(field_name='fecha_inicio', lookup_expr='gte')
    fecha_inicio_hasta = django_filters.DateFilter(field_name='fecha_inicio', lookup_expr='lte')
    organismo = django_filters.ModelChoiceFilter(
        field_name='responsables',
        queryset=Organismo.objects.filter(activo=True)
    )

    class Meta:
        model = Medida
        fields = {
            'componente': ['exact'],
            'estado': ['exact', 'in'],
            'prioridad': ['exact', 'in'],
        }


class RegistroAvanceFilter(django_filters.FilterSet):
    """Filtros avanzados para el endpoint de registros de avance"""
    fecha_desde = django_filters.DateFilter(field_name='fecha_registro', lookup_expr='gte')
    fecha_hasta = django_filters.DateFilter(field_name='fecha_registro', lookup_expr='lte')
    avance_min = django_filters.NumberFilter(field_name='porcentaje_avance', lookup_expr='gte')
    avance_max = django_filters.NumberFilter(field_name='porcentaje_avance', lookup_expr='lte')

    class Meta:
        model = RegistroAvance
        fields = {
            'medida': ['exact'],
            'organismo': ['exact'],
        }