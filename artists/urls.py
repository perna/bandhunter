from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_artists, name="artists-list"),
    url(r'^adicionar$', views.create_artist, name="artists-create"),
]