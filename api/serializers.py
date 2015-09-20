from rest_framework import serializers
from api.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Usuario
        fields = ('id','email','facebook_id','estado','telefono', 'fecha_registro', 'direccion')