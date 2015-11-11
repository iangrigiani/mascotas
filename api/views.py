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
from api.serializers import AdopcionListSerializer
from api.models import DenunciaPublicacion
from api.serializers import DenunciaPublicacionSerializer
from api.serializers import DenunciaPublicacionListSerializer
from api.models import DenunciaUsuario
from api.serializers import DenunciaUsuarioSerializer
from api.serializers import DenunciaUsuarioListSerializer
from api.filters import DenunciaPublicacionListFilter
from api.filters import DenunciaPublicacionFilter
from api.filters import DenunciaUsuarioListFilter
from api.filters import DenunciaUsuarioFilter


class UsuarioViewSet(viewsets.ModelViewSet):
     
    model = Usuario
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_class = UsuarioFilter
    ordering_fields = '__all__'
    search_fields = ('email', 'facebook_id', 'estado', 'telefono', 'fecha_registro', 'direccion')


class TipoMascotaViewSet(viewsets.ModelViewSet):
     
    model = TipoMascota
    queryset = TipoMascota.objects.all()
    serializer_class = TipoMascotaSerializer
    #filter_class = UsuarioFilter
    search_fields = ('tipo')
    ordering_fields = '__all__'
         

class MascotaViewSet(viewsets.ModelViewSet):
     
    model = Mascota
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    filter_class = MascotaFilter
    search_fields = ('nombre', 'raza', 'tipo')
    #ordering_fields = '__all__'

    
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


class AdopcionListViewSet(viewsets.ModelViewSet):
     
    model = Adopcion
    queryset = Adopcion.objects.all()
    serializer_class = AdopcionListSerializer
    filter_class = AdopcionFilter
    search_fields = ('id')
    ordering_fields = '__all__'
    

class DenunciaPublicacionViewSet(viewsets.ModelViewSet):
     
    model = DenunciaPublicacion
    queryset = DenunciaPublicacion.objects.all()
    serializer_class = DenunciaPublicacionSerializer
    filter_class = DenunciaPublicacionFilter
    search_fields = ('id')
    ordering_fields = '__all__'


class DenunciaPublicacionListViewSet(viewsets.ModelViewSet):
     
    model = DenunciaPublicacion
    queryset = DenunciaPublicacion.objects.all()
    serializer_class = DenunciaPublicacionListSerializer
    filter_class = DenunciaPublicacionListFilter
    search_fields = ('id')
    ordering_fields = '__all__'


class DenunciaUsuarioViewSet(viewsets.ModelViewSet):
     
    model = DenunciaUsuario
    queryset = DenunciaUsuario.objects.all()
    serializer_class = DenunciaUsuarioSerializer
    filter_class = DenunciaUsuarioFilter
    search_fields = ('id')
    ordering_fields = '__all__'


class DenunciaUsuarioListViewSet(viewsets.ModelViewSet):
     
    model = DenunciaUsuario
    queryset = DenunciaUsuario.objects.all()
    serializer_class = DenunciaUsuarioListSerializer
    filter_class = DenunciaUsuarioListFilter
    search_fields = ('id')
    ordering_fields = '__all__'
    