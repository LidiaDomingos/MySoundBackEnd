from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/musicas/<int:musica_id>/', views.api_musica),
    path('api/musicas/', views.api_musica_get),
    path('api/playlists/', views.api_playlist_get),
]