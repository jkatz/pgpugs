from django.contrib.auth.models import User
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey('Region', related_name='countries')

    def __unicode__(self):
        return self.name

class Pug(models.Model):
    """
        basic information about a PUG
    """
    name = models.CharField(max_length=255)
    country = models.ForeignKey('Country', related_name='pugs')
    slug = models.SlugField(null=True, unique=True)
    url = models.URLField(verify_exists=False)
    notes = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

class PugAuthor(models.Model):
    """ 
        A relationship table between pugs and authors
    """
    user = models.ForeignKey(User, related_name='pug_authors')
    pug = models.ForeignKey('Pug', related_name='pug_authors')

    def full_name(self):
        return self.user.get_full_name()

    def __unicode__(self):
        return "%s %s" % (self.user, self.pug)

class Post(models.Model):
    """
        A blog post from a user
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(null=True, unique=True)
    url = models.URLField(verify_exists=False, null=True, blank=True)
    author = models.ForeignKey('PugAuthor', related_name='posts')
    date_published = models.DateTimeField(null=False)

    def __unicode__(self):
        return self.title


class Region(models.Model):
    name = models.CharField(max_length=16)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.name