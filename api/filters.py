from rest_framework.compat import django_filters
from api.models import Usuario
from api.models import Mascota
from api.models import MultimediaMascota
from api.models import Publicacion
from api.models import Adopcion
from api.models import DenunciaPublicacion
from api.models import DenunciaUsuario
 
class UsuarioFilter(django_filters.FilterSet):
     
    email = django_filters.CharFilter(lookup_type='icontains',name="email")
    facebook_id = django_filters.CharFilter(lookup_type='iexact',name="facebook_id")
    estado = django_filters.NumberFilter(name="estado")
    telefono = django_filters.CharFilter(lookup_type='iexact',name="telefono")
    direccion = django_filters.CharFilter(lookup_type='icontains',name="direccion")
          
    class Meta:
        model = Usuario
        fields = ['email','facebook_id','estado','telefono','direccion']
        
class MascotaFilter(django_filters.FilterSet):
    tipo = django_filters.CharFilter(lookup_type='iexact',name="tipo__tipo")
    
    class Meta:
        model = Mascota
        fields = ['nombre', 'raza', 'tipo']
        
        
class PublicacionFilter(django_filters.FilterSet):

    SEXO_CHOICES = (  ('Macho', 'Macho'),
                      ('Hembra', 'Hembra'),)
    TAMANIO_CHOICES = (('Pequenio', 'Pequenio'),
                      ('Mediano', 'Mediano'),
                      ('Grande', 'Grande'),)

    
    mascota = django_filters.CharFilter(lookup_type='iexact',name="mascota__tipo__tipo")
    fecha_publicacion_min = django_filters.DateFilter(lookup_type='gte', name="fecha_publicacion")
    fecha_publicacion_max = django_filters.DateFilter(lookup_type='lte', name="fecha_publicacion")
    aviso = django_filters.CharFilter(lookup_type='iexact',name="aviso__tipo")
    sexo = django_filters.MultipleChoiceFilter(choices=SEXO_CHOICES,name="mascota__sexo")
    edad_min = django_filters.CharFilter(lookup_type='gte',name="mascota__edad")
    edad_max = django_filters.CharFilter(lookup_type='lte',name="mascota__edad")
    tamanio = django_filters.MultipleChoiceFilter(choices=TAMANIO_CHOICES,name="mascota__tamanio")
    compatible_chicos = django_filters.NumberFilter(name="mascota__compatible_chicos")
    estado_usuario = django_filters.NumberFilter(name="usuario__estado")

    
    class Meta:
        model = Publicacion
        fields = ['usuario', 'aviso', 'mascota', 'en_transito', 'fecha_publicacion_min', 'fecha_publicacion_max', 'estado', 
                  'sexo', 'edad_min', 'edad_max', 'tamanio', 'compatible_chicos', 'estado_usuario']



class MultimediaMascotaFilter(django_filters.FilterSet):
    tipo = django_filters.CharFilter(lookup_type='iexact',name="tipo")
    id_publicacion = django_filters.NumberFilter(name="id_publicacion")
    
    class Meta:
        model = MultimediaMascota
        fields = ['tipo', 'id_publicacion']
        
        
class AdopcionFilter(django_filters.FilterSet):
    id_publicacion = django_filters.NumberFilter(name="publicacion")
    id_usuario = django_filters.NumberFilter(name="usuario")
    concretada = django_filters.NumberFilter(name="concretada")
    
    class Meta:
        model = Adopcion
        fields = ['id_publicacion','id_usuario','concretada']
        


class DenunciaPublicacionListFilter(django_filters.FilterSet):
    estado_publicacion = django_filters.NumberFilter(name="id_publicacion__estado")
    
    class Meta:
        model = DenunciaPublicacion
        fields = ['estado_publicacion']


class DenunciaPublicacionFilter(django_filters.FilterSet):
    estado_publicacion = django_filters.NumberFilter(name="id_publicacion__estado")
    
    class Meta:
        model = DenunciaPublicacion
        fields = ['estado_publicacion']


class DenunciaUsuarioListFilter(django_filters.FilterSet):
    estado_usuario = django_filters.NumberFilter(name="id_mensaje__usuario__estado")
    
    class Meta:
        model = DenunciaUsuario
        fields = ['estado_usuario']


class DenunciaUsuarioFilter(django_filters.FilterSet):
    estado_usuario = django_filters.NumberFilter(name="id_mensaje__usuario__estado")
    
    class Meta:
        model = DenunciaUsuario
        fields = ['estado_usuario']