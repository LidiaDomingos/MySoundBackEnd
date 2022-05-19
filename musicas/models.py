from django.db import models

class Playlist(models.Model):
    playlist = models.CharField(max_length=200, primary_key=True)
    def __str__(self):
        return f"{self.playlist}"

class Musica(models.Model):
    title = models.CharField(max_length=200)
    artista = models.CharField(max_length=200)
    idp = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    duracao = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    

    playlist = models.ForeignKey(Playlist, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.id}. {self.title} - {self.artista}"