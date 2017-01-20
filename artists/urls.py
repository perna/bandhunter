from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_artists, name="artists-list"),
    url(r'^adicionar/$', views.create_artist, name="artists-create"),
    url(r'^editar/(?P<id_artist>\d+)$', views.update_artist, name="artists-update"),
    url(r'^excluir/(?P<id_artist>\d+)$', views.delete_artist, name="artists-delete"),
]