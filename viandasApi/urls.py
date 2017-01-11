from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from auth import views
from pedidos.views import ProveedorViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

router.register(r'proveedores', ProveedorViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'viandasApi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api/', include(router.urls)),

]
