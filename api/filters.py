from rest_framework.compat import django_filters
from api.models import Usuario
from api.models import Mascota
 
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
    tipo = django_filters.NumberFilter(name="tipo")
    
    class Meta:
        model = Mascota
        fields = ['id','nombre', 'raza', 'tipo']