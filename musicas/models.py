from django.db import models

class Playlist(models.Model):
    playlist = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id}. {self.playlist}"

class Musica(models.Model):
    title = models.CharField(max_length=200)
    artista = models.CharField(max_length=200)
    idp = models.IntegerField(null=True)

    playlist = models.ForeignKey(Playlist, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.id}. {self.title} - {self.artista}"