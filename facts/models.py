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
    song = models.ForeignKey(Song, on_delete=models.PROTECT)
    content = models.TextField()
    writtenBy = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.content} \n נכתב על ידי {self.writtenBy}"


