from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from artists.models import Artist


@login_required
def index(request):
    try:
        artist = Artist.objects.get(user=request.user)
    except Artist.DoesNotExist:
        artist = None
    context = {'artist': artist}
    return render(request, 'dashboard/index.html', context)
