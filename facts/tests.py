from django.test import TestCase
from .models import Artist, Song, Fact


class FactTests(TestCase):
    def test_create_items(self):
        mashina = Artist.objects.create(
            name='mashina',
        )
        train = mashina.song_set.create(
            title='train to cairo'
        )
        train.fact_set.create(
            content="great song!",
            writtenBy="mashina",
        )
