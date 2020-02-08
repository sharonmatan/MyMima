from bs4 import BeautifulSoup
import requests
from facts.models import Artist, Song, Fact
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        for id in range(1, 10):
            r = requests.get(f"https://www.mima.co.il/fact_page.php?song_id={id}")
            soup = BeautifulSoup(r.text, 'html.parser')
            song_name = soup.find('font', size="+5").get_text()
            artist_name = soup.find('font', size="+2").get_text()
            facts = soup.findAll('tr', bgcolor=['#CCFFCC', "#EDF3FE"])
            # fact_written_by = soup.find('font', size="-1").get_text()
            artist, created = Artist.objects.get_or_create(name=artist_name)
            song, created = Song.objects.get_or_create(artist=artist, title=song_name)
            for fact in facts:
                facts, created = Fact.objects.get_or_crSSSeate(song=song, content=fact.text)
            # fact_written, created = Fact.objects.get_or_create(written_by=fact_written_by)

