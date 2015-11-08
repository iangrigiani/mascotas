from django.conf.urls import include, url
from rest_framework import routers
from api.views import UsuarioViewSet
from api.views import MascotaViewSet
from api.views import TipoMascotaViewSet
from api.views import PublicacionViewSet
from api.views import TipoAvisoViewSet
from api.views import MultimediaViewSet
from api.views import MensajeViewSet
from api.views import AdopcionViewSet
from api.views import AdopcionListViewSet
from api.views import DenunciaPublicacionViewSet
from api.views import DenunciaPublicacionListViewSet
from api.views import DenunciaUsuarioViewSet
from api.views import DenunciaUsuarioListViewSet


router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'mascotas', MascotaViewSet)
router.register(r'tipo_mascotas', TipoMascotaViewSet)
router.register(r'publicaciones', PublicacionViewSet)
router.register(r'tipo_avisos', TipoAvisoViewSet)
router.register(r'multimedias', MultimediaViewSet)
router.register(r'mensajes', MensajeViewSet)
router.register(r'adopciones_list', AdopcionListViewSet)
router.register(r'adopciones', AdopcionViewSet)
router.register(r'denuncia_publicacion_list', DenunciaPublicacionListViewSet)
router.register(r'denuncia_publicacion', DenunciaPublicacionViewSet)
router.register(r'denuncia_usuario_list', DenunciaUsuarioListViewSet)
router.register(r'denuncia_usuario', DenunciaUsuarioViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
