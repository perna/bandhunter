from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Artist

def index(request):
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