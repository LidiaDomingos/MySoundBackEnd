from rest_framework import serializers
from .models import Musica, Playlist


class MusicaSerializer(serializers.ModelSerializer):
    playlist = serializers.ReadOnlyField(source='playlist.playlist')
    class Meta:
        model = Musica
        fields = ['id', 'title', 'artista','playlist','idp', 'img', 'link', 'album', 'duracao' ]

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['playlist']