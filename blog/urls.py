from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas),
    url(r'^$', views.usuario_nueva),
    url(r'^usario/nueva/$', views.usuario_nueva, name='usuario_nueva'),
]
