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
    country = models.ForeignKey(Country, related_name='pugs')
    slug = models.SlugField(null=True, unique=True)
    url = models.URLField(verify_exists=False)
    notes = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=16)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.name