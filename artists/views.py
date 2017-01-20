from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
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


@login_required
def create_artist(request):
    form = ArtistForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('dashboard-index')

    context = {'form': form}
    return render(request, 'artists/form.html', context)


@login_required
def update_artist(request, id_artist):
    artist = Artist.objects.get(pk=id_artist)

    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)

        if form.is_valid():
            form.save()
            return redirect('artists-list')
    else:
        form = ArtistForm(instance=artist)
        context = {'form': form}
        return render(request, 'artists/form.html', context)


@login_required
def delete_artist(request, id_artist):
    artist = Artist.objects.get(pk=id_artist)

    if request.method == "POST":
        artist.delete()
        return redirect('artists-list')

    else:
        return render(request, 'artists/form.html')
