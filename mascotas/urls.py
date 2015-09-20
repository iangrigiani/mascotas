from django.conf.urls import include, url
from rest_framework import routers
from api.views import UsuarioViewSet



router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
