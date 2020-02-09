from django.shortcuts import render, get_object_or_404, redirect
from facts.models import Song, Artist, Fact
from .forms import SearchString

from . import forms
from .forms import SearchString

letters_list = []
for i in range(1488, 1515):
    if i not in (1498, 1501, 1503, 1507, 1509):
        letters_list.append(chr(i))


def homepage_start(request):
    return render(request, "facts/homepage.html", {'letters_list': letters_list})


def base(request):
    return render(request, "facts/base.html", {'letters_list': letters_list})


def song(request, id):
    song = get_object_or_404(Song, id=id)
    return render(request, "facts/song_page.html", {'song': song})


def song_start_with(request, letter):
    list_of_songs = Song.objects.filter(title__startswith=letter)
    context = {
        'list_of_songs': list_of_songs,
    }
    return render(request, 'facts/song_start_with.html', context)


def artist_start_with(request, letter):
    list_of_artists = Artist.objects.filter(name__startswith=letter)
    context = {
        'list_of_artists': list_of_artists,
    }
    return render(request, 'facts/artist_start_with.html', context)


def artist_songs(request, id):
    artist = get_object_or_404(Artist, id=id)
    return render(request, 'facts/artist_songs.html', {"artist": artist})


def search_results(request):
    x = str(request.GET["search"])
    print(x)
    list_of_artists = Artist.objects.filter(name__contains=x)
    print(list_of_artists)
    list_of_songs = Song.objects.filter(title__contains=x)
    list_of_facts = Fact.objects.filter(content__contains=x)
    context = {'list_of_artists': list_of_artists,
               'list_of_songs': list_of_songs,
               'list_of_facts': list_of_facts,
               }

    return render(request, 'facts/list_songs_artists_facts.html', context)
