from django import forms
from .models import Artist


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'press_release', 'genres', 'photo', 'phone', 'site', 'contact_email',
                  'facebook', 'instagram', 'twitter', 'snapchat'
                  ]


SEARCH_OPTIONS = (('1', 'Por nome'), ('2', 'Por descrição'), ('3', 'Por gênero'),)


class SearchForm(forms.Form):
        query_search = forms.CharField(label="Busca", required=True,)
        search_option = forms.ChoiceField(label="Filtrar busca", widget=forms.Select,
                                          choices=SEARCH_OPTIONS, initial='1')
