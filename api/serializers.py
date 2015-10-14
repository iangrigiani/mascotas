from rest_framework import serializers
from api.models import Usuario
from api.models import Mascota
from api.models import Publicacion
from api.models import TipoMascota
from api.models import TipoAviso
from api.models import MultimediaMascota
from api.models import Mensaje


class UsuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Usuario
        fields = ('id','nombre', 'apellido', 'email','facebook_id','estado','telefono', 'fecha_registro', 'direccion', 'latitud', 'longitud', 'foto_perfil_url')
        
        
class TipoMascotaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TipoMascota
        fields =('id', 'tipo')
        

class MultimediaMascotaSerializer(serializers.ModelSerializer):
    
#     id_publicacion = serializers.SlugRelatedField(
#         slug_field='id',
#         queryset=Publicacion.objects.all()
#     )
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = MultimediaMascota
        fields = ('id','tipo','url','orden')



class MascotaSerializer(serializers.ModelSerializer):
    
    tipo = serializers.SlugRelatedField(        
        slug_field='tipo',
        queryset=TipoMascota.objects.all()
    )

    class Meta:
        model = Mascota
        fields = ('id','nombre','raza','tipo', 'sexo', 'edad', 'tamanio', 'compatible_chicos', 'medicacion')



class TipoAvisoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TipoAviso
        fields =('id', 'tipo')


class MensajeSerializer(serializers.ModelSerializer):
    
    id_publicacion = serializers.SlugRelatedField(
        slug_field='id',
        queryset=Publicacion.objects.all()
    )

    class Meta:
        model = Mensaje
        fields = ('id','usuario', 'id_publicacion','fecha_publicacion','texto')


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
    multimedia = MultimediaMascotaSerializer(many=True)
    mensajes = MensajeSerializer(many=True)

    class Meta:
        model = Publicacion
        fields = ('id', 'mascota', 'usuario', 'aviso', 'en_transito', 'fecha_publicacion', 'estado', 'latitud', 
                  'longitud', 'multimedia', 'descripcion', 'mensajes')
        
        
    def create(self, validated_data):

        mascota_data = validated_data.pop('mascota')

        mascota_obj = Mascota(nombre=mascota_data.pop('nombre'), raza=mascota_data.pop('raza'), tipo=mascota_data.pop('tipo'), sexo=mascota_data.pop('sexo'),
                              edad=mascota_data.pop('edad'), tamanio=mascota_data.pop('tamanio'), compatible_chicos=mascota_data.pop('compatible_chicos'), 
                              medicacion=mascota_data.pop('medicacion'))
        mascota_obj.save()
   
        publicacion = Publicacion(usuario=validated_data.pop('usuario'), 
            aviso=validated_data.pop('aviso'),  en_transito=validated_data.pop('en_transito'), 
            estado=validated_data.pop('estado'), latitud=validated_data.pop('latitud'), longitud=validated_data.pop('longitud'), descripcion=validated_data.pop('descripcion'))
        publicacion.mascota = mascota_obj

        publicacion.save()
       
        for multimedia_obj in validated_data.pop('multimedia'):
            multimedia = MultimediaMascota(tipo=multimedia_obj.pop('tipo'),url=multimedia_obj.pop('url'),orden=multimedia_obj.pop('orden') )
            multimedia.id_publicacion = publicacion
            multimedia.save()
                
        return publicacion
    
    
    def update(self, instance, validated_data):

        
        mascota = instance.mascota
        mascota_data = validated_data.pop('mascota')
            
        mascota.nombre=mascota_data.pop('nombre')
        mascota.raza=mascota_data.pop('raza')
        mascota.tipo=mascota_data.pop('tipo')
        mascota.sexo=mascota_data.pop('sexo')
        mascota.edad=mascota_data.pop('edad')
        mascota.tamanio=mascota_data.pop('tamanio')
        mascota.compatible_chicos=mascota_data.pop('compatible_chicos')
        mascota.medicacion=mascota_data.pop('medicacion')
  
        mascota.save()
           
        instance.usuario=validated_data.pop('usuario')
        instance.aviso=validated_data.pop('aviso')
        instance.en_transito=validated_data.pop('en_transito')
        instance.estado=validated_data.pop('estado')
        instance.latitud=validated_data.pop('latitud')
        instance.longitud=validated_data.pop('longitud')
        instance.descripcion=validated_data.pop('descripcion')        
            
        instance.save()

        multimedia_array = MultimediaMascota.objects.filter(id_publicacion=instance.id)
               
        for multimedia_viejo in multimedia_array:
            multimedia_viejo.delete()
 
        for multimedia_obj in validated_data['multimedia']:
            multimedia = MultimediaMascota(tipo=multimedia_obj.pop('tipo'),url=multimedia_obj.pop('url'),orden=multimedia_obj.pop('orden'))
            multimedia.id_publicacion = instance
            multimedia.save()

        return instance
   