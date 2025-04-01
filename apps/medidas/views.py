from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Medida, LogMedida
from .serializers import MedidaSerializer

# Create your views here.
class MedidaViewSet(viewsets.ModelViewSet):
    # TODO: we should modify this .all to follow best practices
    queryset = Medida.objects.filter(activo=True)
    serializer_class = MedidaSerializer
    #permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        medida = serializer.save(usuario=self.request.user)
        LogMedida.objects.create(usuario=self.request.user, medida=medida, accion="crear")
        
    def perform_update(self, serializer):
        medida = serializer.save()
        LogMedida.objects.create(usuario=self.request.user, medida=medida, accion="actualizar")
        
    def destroy(self, instance, *args, **kwargs):
        """Soft delete: instead of deleting, set activo=False"""
        instance = self.get_object()
        instance.activo = False
        instance.save()
        
        # Log the delete action
        LogMedida.objects.create(usuario=self.request.user, medida=instance, accion="eliminar")
        return Response({"message": "Medida archived instead of deleted"}, status=status.HTTP_204_NO_CONTENT)