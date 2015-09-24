from rest_framework import serializers
from api.models import Usuario
from api.models import Mascota
from api.models import Publicacion
from api.models import TipoMascota
from api.models import TipoAviso
from api.models import MultimediaMascota


class UsuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Usuario
        fields = ('id','email','facebook_id','estado','telefono', 'fecha_registro', 'direccion', 'foto_perfil_url')
        
        
class TipoMascotaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TipoMascota
        fields =('id', 'tipo')
        

class MultimediaMascotaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MultimediaMascota
        fields = ('id','id_mascota','tipo','url', 'orden')



class MascotaSerializer(serializers.ModelSerializer):
    
    tipo = serializers.SlugRelatedField(        
        slug_field='tipo',
        queryset=TipoMascota.objects.all()
    )
#     multimedia = MultimediaMascotaSerializer()
    
    class Meta:
        model = Mascota
        fields = ('id','nombre','raza','tipo')



class TipoAvisoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TipoAviso
        fields =('id', 'tipo')


class PublicacionSerializer(serializers.ModelSerializer):
    

    mascota = MascotaSerializer()
    usuario = serializers.SlugRelatedField(
        slug_field='id', 
        queryset=Usuario.objects.all()
    )
    aviso = serializers.SlugRelatedField(
        slug_field='tipo', 
        queryset=TipoAviso.objects.all()
    )

    class Meta:
        model = Publicacion
        fields = ('id', 'mascota', 'usuario', 'aviso', 'en_transito', 'estado', 'latitud', 'longitud')
        
        
    def create(self, validated_data):

        mascota_data = validated_data.pop('mascota')
        mascota_obj = Mascota(nombre=mascota_data.pop('nombre'), raza=mascota_data.pop('raza'), tipo=mascota_data.pop('tipo'))
        mascota_obj.save()

        publicacion = Publicacion(usuario=validated_data.pop('usuario'), 
            aviso=validated_data.pop('aviso'),  en_transito=validated_data.pop('en_transito'), 
            estado=validated_data.pop('estado'), latitud=validated_data.pop('latitud'), longitud=validated_data.pop('longitud'))
        publicacion.mascota = mascota_obj
        
        publicacion.save()
        
        return publicacion
    
    
    
   