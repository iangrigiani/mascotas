from django.conf.urls import include, url
from rest_framework import routers
from api.views import UsuarioViewSet
from api.views import MascotaViewSet
from api.views import TipoMascotaViewSet



router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'mascotas', MascotaViewSet)
router.register(r'tipo_mascotas', TipoMascotaViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
