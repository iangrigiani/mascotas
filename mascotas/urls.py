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

urlpatterns = [
    url(r'^', include(router.urls)),
]
