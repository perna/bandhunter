from django.db import models
from django.db.models import signals
from django.core.urlresolvers import reverse
from .signals import create_slug
from taggit.managers import TaggableManager

from django.contrib.auth.models import User
import hashlib
import random


def photo_path_and_name(instance, filename):
    random_filename = hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()
    path = 'artists/'
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (random_filename, ext)
    return '/'.join([path, filename, ])


class Artist(models.Model):
    name = models.CharField("Nome", max_length=120)
    press_release = models.TextField("Press Release", db_index=True)
    photo = models.ImageField("Foto", upload_to=photo_path_and_name)
    phone = models.CharField("Telefone", max_length=20)
    site = models.CharField("Site", max_length=200, blank=True)
    contact_email = models.EmailField("Email")
    facebook = models.CharField("Facebook", max_length=255, blank=True, null=True)
    instagram = models.CharField("Instagram", max_length=120, blank=True, null=True)
    twitter = models.CharField("Twitter", max_length=120, blank=True, null=True)
    snapchat = models.CharField("Snapchat", max_length=120, blank=True, null=True)
    slug = models.SlugField(max_length=170, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    genres = TaggableManager(verbose_name="Gênero Musical", blank=True)
    slug_field_name = 'slug'
    slug_from = 'name'
    user = models.OneToOneField(User)

    class Meta:
        db_table = 'artist'
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("artist-profile", kwargs={'pk': self.pk})


signals.post_save.connect(create_slug, sender=Artist)
