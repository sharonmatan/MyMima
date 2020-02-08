from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT)
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Fact(models.Model):
    song = models.ForeignKey(Song, on_delete=models.PROTECT, related_name='facts')
    content = models.TextField()
    # written_by = models.CharField(max_length=150)

    def __str__(self):
        return self.content

