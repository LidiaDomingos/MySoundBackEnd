from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Musica, Playlist
from .serializers import MusicaSerializer, PlaylistSerializer


# SUAS OUTRAS FUNÇÕES CONTINUAM AQUI

from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")


@api_view(['GET', 'POST', 'DELETE'])
def api_musica(request, musica_id):
    try:
        musica = Musica.objects.get(id=musica_id)
    except Musica.DoesNotExist:
        raise Http404()

    if request.method == "DELETE":
        musica.delete()
        return Response(status=204)

    # all_notes = Note.objects.all()
    serialized_musica = MusicaSerializer(musica)
    return Response(serialized_musica.data)

@api_view(['GET', 'POST', ])
def api_musica_get(request):

    if request.method == 'POST':
        new_musica_data = request.data
        title = new_musica_data['title']
        artista = new_musica_data['artista']
        playlist = new_musica_data['playlist']
        idp = new_musica_data['idp']
        img = new_musica_data['img']
        duracao = new_musica_data['duracao']
        link = new_musica_data['link']
        album = new_musica_data['album']

        print("#########################################")
        print(playlist)

        playlist = playlist.replace(" ","_")

        if Playlist.objects.filter(playlist=playlist).exists() == False:
            playlistNova = Playlist(playlist=playlist)
            playlistNova.save()
            playlist = playlistNova
        else:
            playlist = Playlist.objects.get(playlist=playlist)    

        new_musica = Musica(title=title, artista=artista, playlist=playlist, idp=idp, img=img,album=album, link=link, duracao=duracao)
        new_musica.save()

    all_musicas = Musica.objects.all()
    serialized_musica = MusicaSerializer(all_musicas, many=True)
    return Response(serialized_musica.data)

@api_view(['GET', 'POST', ])
def api_playlist_get(request):
    all_playlist = Playlist.objects.all()
    serialized_playlist = PlaylistSerializer(all_playlist, many=True)
    return Response(serialized_playlist.data)

@api_view(['GET', 'POST', 'DELETE'])
def api_playlist(request, playlist):
    try:
        playlist = Playlist.objects.get(playlist=playlist)
    except Playlist.DoesNotExist:
        raise Http404()

    if request.method == "DELETE":
        playlist.delete()
        return Response(status=204)

    all_musicas = Musica.objects.filter(playlist=playlist)
    serialized_musica = MusicaSerializer(all_musicas, many=True)
    return Response(serialized_musica.data)
