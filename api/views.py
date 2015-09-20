from rest_framework import viewsets
from api.models import Usuario
from api.serializers import UsuarioSerializer
from api.filters import UsuarioFilter


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
        """
        Crea un nuevo usuario.
        """
        return viewsets.ModelViewSet.create(self, request, *args, **kwargs)
    
    #put    
    def update(self, request, pk=None, *args, **kwargs):
        """
        Actualiza un usuario completo.
        """
        return viewsets.ModelViewSet.update(self, request, *args, **kwargs)

    #delete
    def destroy(self, request, pk=None, *args, **kwargs):
        """
        Elimina un usuario.
        """
        return viewsets.ModelViewSet.destroy(self, request, *args, **kwargs)

