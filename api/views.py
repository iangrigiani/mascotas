from rest_framework import viewsets
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
from api.models import MultimediaMascota
from api.serializers import MultimediaMascotaSerializer
from api.filters import MultimediaMascotaFilter
from api.models import Mensaje
from api.serializers import MensajeSerializer
from api.models import Adopcion
from api.serializers import AdopcionSerializer
from api.filters import AdopcionFilter

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
    search_fields = ('mascota', 'usuario', 'aviso', 'en_transito', 'fecha_publicacion', 'estado', 'latitud', 'longitud', 'multimedia', 'descripcion')
    #ordering_fields = '__all__'


    def list(self, request, *args, **kwargs):
        """
        Lista todos los usuarios.
        """
        
        latitud = request.GET.get('latitud')
        longitud = request.GET.get('longitud')
        distancia = request.GET.get('distancia')
        
        # Por defecto centrado en FIUBA y con 3k de distancia
        if latitud==None:
            latitud=-34.606515
        if longitud==None:
            longitud=-58.435766
        if distancia==None:
            distancia=3000
            
        
        self.queryset = Publicacion.objects.in_distance(distancia, ('latitud', 'longitud'), (latitud, longitud))

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
    
    
class MultimediaViewSet(viewsets.ModelViewSet):
     
    model = MultimediaMascota
    queryset = MultimediaMascota.objects.all()
    serializer_class = MultimediaMascotaSerializer
    filter_class = MultimediaMascotaFilter
    search_fields = ('url')
    ordering_fields = '__all__'


class MensajeViewSet(viewsets.ModelViewSet):
     
    model = Mensaje
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer
    #filter_class = UsuarioFilter
    search_fields = ('id')
    ordering_fields = '__all__'


class AdopcionViewSet(viewsets.ModelViewSet):
     
    model = Adopcion
    queryset = Adopcion.objects.all()
    serializer_class = AdopcionSerializer
    filter_class = AdopcionFilter
    search_fields = ('id')
    ordering_fields = '__all__'
