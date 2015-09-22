from rest_framework.compat import django_filters
from api.models import Usuario
from api.models import Mascota
from api.models import Publicacion
 
class UsuarioFilter(django_filters.FilterSet):
     
    email = django_filters.CharFilter(lookup_type='icontains',name="email")
    facebook_id = django_filters.CharFilter(lookup_type='iexact',name="facebook_id")
    estado = django_filters.NumberFilter(lookup_type='iexact',name="estado")
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
    mascota = django_filters.CharFilter(lookup_type='iexact',name="mascota__tipo__tipo")
    aviso = django_filters.CharFilter(lookup_type='iexact',name="aviso__tipo")
    
    class Meta:
        model = Publicacion
        fields = ['usuario', 'aviso', 'mascota', 'en_transito', 'estado']
