from rest_framework import serializers
from .models import Musica, Playlist


class MusicaSerializer(serializers.ModelSerializer):
    playlist = serializers.ReadOnlyField(source='playlist.playlist')
    class Meta:
        model = Musica
        fields = ['id', 'title', 'artista', 'playlist']

