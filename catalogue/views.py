from django.shortcuts import render
from .models import Artist


def index(request):
    artists = Artist.objects.all()
    return render(request, 'catalogue/index.html', {
        'artists': artists
    })