from django.db import models
from django.contrib.auth.models import User

from tagging.fields import TagField
from tagging.models import Tag
from tagging_autocomplete.models import TagAutocompleteField
<<<<<<< HEAD
from timezones.fields import TimeZoneField


class Profile(models.Model):
    user = models.OneToOneField(User)
    skype = models.CharField("Skype ID", max_length=20, null=True, blank=True)
    aim = models.CharField("AIM", max_length=20, null=True, blank=True)
    gchat = models.CharField("Google Chat", max_length=20, null=True, blank=True)
    phone = models.CharField("Phone number", max_length=20, null=True, blank=True)
    timezone = TimeZoneField()

=======

class Profile(models.Model):
    user = models.OneToOneField(User)
>>>>>>> 3f3a784d2ebea8c8e7104cfb80e1c547b051eeac
    skills = models.ManyToManyField('Skill', blank=True)
    def __unicode__(self):
        return unicode(self.user)

class Skill(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
