from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Artist
from .forms import ArtistForm


def list_artists(request):
    artist_list = Artist.objects.all()
    paginator = Paginator(artist_list, 10)
    page = request.GET.get('page', 1)

    try:
        artists = paginator.page(page)
    except PageNotAnInteger:
        artists = paginator.page(1)
    except EmptyPage:
        artists = paginator.page(paginator.num_pages)

    context = {'artists': artists}
    return render(request, 'artists/index.html', context)


def create_artist(request):
    form = ArtistForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('artists-list')

    context = {'form': form}
    return render(request, 'artists/form.html', context)