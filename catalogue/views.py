from django.shortcuts import render, get_object_or_404
from .models import Artist


def index(request):
    artists = Artist.objects.all()
    return render(request, 'catalogue/index.html', {
        'artists': artists
    })


def show(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    return render(request, 'catalogue/show.html', {
        'artist': artist
    })