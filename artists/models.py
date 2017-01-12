from django.db import models
from django.utils.text import slugify
import itertools

class Artist(models.Model):
    name = models.CharField("Nome", max_length=120)
    press_release = models.TextField("Press Release", db_index=True)
    photo = models.ImageField("Foto")
    phone = models.CharField("Telefone", max_length=20)
    site = models.CharField("Site", max_length=200)
    contact_email = models.EmailField("Email")
    facebook = models.CharField("Facebook", max_length=255, blank=False, null=True)
    instagram = models.CharField("Instagram", max_length=120, blank=False, null=True)
    twitter = models.CharField("Twitter", max_length=120, blank=False, null=True)
    snapchat = models.CharField("Snapchat", max_length=120, blank=False, null=True)
    slug = models.SlugField(max_length=170, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'artist'
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'

    def __str__(self):
        return self.name


    def save(self):
        instance = super(Artist, self).save(commit=False)
        instance.slug = orig = slugify(instance.title)

        for x in itertools.count(1):
            if not Post.objects.filter(slug=instance.slug).exists():
                break
            instance.slug = '%s-%d' % (orig, x)

        instance.save()
        return instance
