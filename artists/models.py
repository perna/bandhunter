from django.db import models
from django.db.models import signals
from django.core.urlresolvers import reverse
from .signals import create_slug
from django.contrib.auth.models import User


class Artist(models.Model):
    name = models.CharField("Nome", max_length=120)
    press_release = models.TextField("Press Release", db_index=True)
    photo = models.ImageField("Foto", upload_to='artists/')
    phone = models.CharField("Telefone", max_length=20)
    site = models.CharField("Site", max_length=200)
    contact_email = models.EmailField("Email")
    facebook = models.CharField("Facebook", max_length=255, blank=False, null=True)
    instagram = models.CharField("Instagram", max_length=120, blank=False, null=True)
    twitter = models.CharField("Twitter", max_length=120, blank=False, null=True)
    snapchat = models.CharField("Snapchat", max_length=120, blank=False, null=True)
    slug = models.SlugField(max_length=170, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
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
