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
    

    mascota = MascotaSerializer()
    usuario = serializers.SlugRelatedField(
        slug_field='id', 
        queryset=Usuario.objects.all()
    )

    class Meta:
        model = Publicacion
        fields = ('id', 'mascota', 'usuario', 'en_transito', 'estado')
        depth=1
        
        
    def create(self, validated_data):

        mascota_data = validated_data.pop('mascota')
        mascota_obj = Mascota(nombre=mascota_data.pop('nombre'), raza=mascota_data.pop('raza'), tipo=mascota_data.pop('tipo'))
        mascota_obj.save()

        publicacion = Publicacion(usuario=validated_data.pop('usuario'), en_transito=validated_data.pop('en_transito'), estado=validated_data.pop('estado'))
        publicacion.mascota = mascota_obj
        
        publicacion.save()
        
        return publicacion
    
    
    
   