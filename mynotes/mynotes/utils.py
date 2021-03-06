import string, random

from django.utils.text import slugify

#Slug generator from Ishwar Jangid
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.subject_text)

    # Klass to the actual model class that the instance comes from.
    Klass = instance.__class__
    #looking up all instances of that particular class that matches lookup call (slug=slug)
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug