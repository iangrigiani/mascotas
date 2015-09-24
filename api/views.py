from rest_framework import viewsets
from djorm_expressions.models import ExpressionManager
from api.models import Usuario
from api.serializers import UsuarioSerializer
from api.filters import UsuarioFilter
from api.models import Mascota
from api.serializers import MascotaSerializer
from api.filters import MascotaFilter
from api.models import TipoMascota
from api.serializers import TipoMascotaSerializer
from api.models import Publicacion
from api.serializers import PublicacionSerializer
from api.filters import PublicacionFilter
from api.models import TipoAviso
from api.serializers import TipoAvisoSerializer



class UsuarioViewSet(viewsets.ModelViewSet):
     
    model = Usuario
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_class = UsuarioFilter
    ordering_fields = '__all__'
    search_fields = ('email', 'facebook_id', 'estado', 'telefono', 'fecha_registro', 'direccion')
         
 
    def list(self, request, *args, **kwargs):
        """
        Lista todos los usuarios.
        """
        return viewsets.ModelViewSet.list(self, request, *args, **kwargs)
 
   
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve el usuario solicitado por id.
        """
        return viewsets.ModelViewSet.retrieve(self, request, *args, **kwargs)
   
    #post
    def create(self, request, *args, **kwargs):
        return viewsets.ModelViewSet.create(self, request, *args, **kwargs)
     
    #put    
    def update(self, request, pk=None, *args, **kwargs):
        return viewsets.ModelViewSet.update(self, request, *args, **kwargs)
 
    #delete
    def destroy(self, request, pk=None, *args, **kwargs):
        return viewsets.ModelViewSet.destroy(self, request, *args, **kwargs)


class TipoMascotaViewSet(viewsets.ModelViewSet):
     
    model = TipoMascota
    queryset = TipoMascota.objects.all()
    serializer_class = TipoMascotaSerializer
    #filter_class = UsuarioFilter
    search_fields = ('tipo')
    ordering_fields = '__all__'
         
 
    def list(self, request, *args, **kwargs):
        return viewsets.ModelViewSet.list(self, request, *args, **kwargs)
   
    #post
    def create(self, request, *args, **kwargs):
        return viewsets.ModelViewSet.create(self, request, *args, **kwargs)


class MascotaViewSet(viewsets.ModelViewSet):
     
    model = Mascota
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    filter_class = MascotaFilter
    search_fields = ('nombre', 'raza', 'tipo')
    #ordering_fields = '__all__'
         
 
    def list(self, request, *args, **kwargs):
        """
        Lista todos los usuarios.
        """
        return viewsets.ModelViewSet.list(self, request, *args, **kwargs)
 
   
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve el usuario solicitado por id.
        """
        return viewsets.ModelViewSet.retrieve(self, request, *args, **kwargs)
   
        #post
    def create(self, request, *args, **kwargs):
        return viewsets.ModelViewSet.create(self, request, *args, **kwargs)
     
    #put    
    def update(self, request, pk=None, *args, **kwargs):
        return viewsets.ModelViewSet.update(self, request, *args, **kwargs)
 
    #delete
    def destroy(self, request, pk=None, *args, **kwargs):
        return viewsets.ModelViewSet.destroy(self, request, *args, **kwargs)
    
    
class PublicacionViewSet(viewsets.ModelViewSet):
     
    model = Publicacion
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer
    filter_class = PublicacionFilter
    search_fields = ('mascota', 'usuario', 'aviso', 'en_transito', 'fecha_publicacion', 'estado', 'latitud', 'longitud')
    #ordering_fields = '__all__'


    def list(self, request, *args, **kwargs):
        """
        Lista todos los usuarios.
        """
        
        latitud = request.GET.get('latitud')
        longitud = request.GET.get('longitud')
        distancia = request.GET.get('distancia')
        
        if latitud==None:
            latitud=0
        if longitud==None:
            longitud=0
        if distancia==None:
            distancia=1000
        
        self.queryset = Publicacion.objects.in_distance(distancia, ('latitud', 'longitud'), (float(latitud), float(longitud)))
        
        return viewsets.ModelViewSet.list(self, request, *args, **kwargs)



class TipoAvisoViewSet(viewsets.ModelViewSet):
     
    model = TipoAviso
    queryset = TipoAviso.objects.all()
    serializer_class = TipoAvisoSerializer
    #filter_class = UsuarioFilter
    search_fields = ('tipo')
    ordering_fields = '__all__'
         
 
    def list(self, request, *args, **kwargs):
        return viewsets.ModelViewSet.list(self, request, *args, **kwargs)
   
    #post
    def create(self, request, *args, **kwargs):
        return viewsets.ModelViewSet.create(self, request, *args, **kwargs)
    
    
         
