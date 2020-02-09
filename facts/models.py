from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)

    def _str_(self):
        return self.title


class Fact(models.Model):
    song = models.ForeignKey(Song, on_delete=models.PROTECT, related_name='facts', blank=True, null=True)
    content = models.TextField()
    written_by = models.CharField(max_length=200, blank=True, null=True)

    def _str_(self):
        return self.content
