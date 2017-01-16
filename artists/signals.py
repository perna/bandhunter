from django.utils.text import slugify

def create_slug(sender, instance, signal, *args, **kwargs):
    if instance.id and hasattr(instance, 'slug_field_name') and hasattr(instance, 'slug_from'):
        slug_name = instance.slug_field_name
        slug_from = instance.slug_from
        if not getattr(instance, slug_name, None):
            slug = "{0}{1}".format(slugify(getattr(instance, slug_from)), str(instance.id))
            setattr(instance, slug_name, slug)
            instance.save()