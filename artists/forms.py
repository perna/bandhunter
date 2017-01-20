from django.forms import ModelForm
from .models import Artist


class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'press_release', 'photo', 'phone', 'site', 'contact_email',
                  'facebook', 'instagram', 'twitter', 'snapchat'
                  ]
