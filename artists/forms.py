from django.forms import ModelForm
from .models import Artist

class ArtistForm(ModelForm):
    class Meta:
        model = Artist