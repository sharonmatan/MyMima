from bs4 import BeautifulSoup
import requests
from facts.models import Artist, Song, Fact
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Closes'

    def handle(self, *args, **options):
        for id in range(1, 20):
            r = requests.get(f"https://www.mima.co.il/fact_page.php?song_id={id}")
            soup = BeautifulSoup(r.text, 'html.parser')
            song_name = soup.find('font', size="+5").get_text()
            artist_name = soup.find('font', size="+2").get_text()
            facts = soup.findAll('tr', bgcolor=['#CCFFCC', "#EDF3FE"])
            artist, created = Artist.objects.get_or_create(name=artist_name)
            song, created = Song.objects.get_or_create(artist=artist, title=song_name)
            for fact in facts:
                fact_seperator = fact.text.strip().split('נכתב ע"י')
                fact_data = fact_seperator[0]
                try:
                    written_by = fact_seperator[1]
                except IndexError:
                    written_by = ''
                fact, created = Fact.objects.get_or_create(song=song, content=fact_data, written_by=written_by)
