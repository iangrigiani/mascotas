from rest_framework import serializers
from api.models import Usuario
from api.models import Mascota
from api.models import Publicacion
from api.models import TipoMascota


class UsuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Usuario
        fields = ('id','email','facebook_id','estado','telefono', 'fecha_registro', 'direccion', 'foto_perfil_url')
        
        
class TipoMascotaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TipoMascota
        fields =('id', 'tipo')
        

class MascotaSerializer(serializers.ModelSerializer):
    
    tipo = serializers.SlugRelatedField(        
        slug_field='tipo',
        queryset=TipoMascota.objects.all()
    )

    class Meta:
        model = Mascota
        fields = ('id','nombre','raza','tipo')


class PublicacionSerializer(serializers.ModelSerializer):
    
#     tipo = serializers.SlugRelatedField(
#         slug_field='tipo',
#         queryset=Publicacion.objects.all()
#     )
    mascota = MascotaSerializer()
    usuario = serializers.SlugRelatedField(
        slug_field='id', 
        queryset=Usuario.objects.all()
    )

    class Meta:
        model = Publicacion
        fields = ('id', 'mascota', 'usuario', 'en_transito', 'fecha_publicacion', 'estado')
   