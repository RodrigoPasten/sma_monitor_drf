from rest_framework import serializers
from .models import Usuario  # Importa el nuevo modelo

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type':'password'})

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password', 'organismo', 'rol']

    def create(self, validated_data):
        user = Usuario.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            organismo=validated_data['organismo'],
            rol=validated_data['rol']
        )
        return user
