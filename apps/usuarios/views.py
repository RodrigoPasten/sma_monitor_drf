from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from apps.usuarios.models import Usuario
from apps.usuarios.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer
    # Usa autenticación basada en token

