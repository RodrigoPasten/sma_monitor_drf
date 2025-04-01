from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.usuarios.views import UserViewSet
from apps.organismos.views import OrganismoViewSet
from apps.medidas.views import MedidaViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'organismos', OrganismoViewSet)
router.register(r'medidas', MedidaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

