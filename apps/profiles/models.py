from django.db import models
from django.contrib.auth.models import User

from tagging.fields import TagField
from tagging.models import Tag
from tagging_autocomplete.models import TagAutocompleteField
from timezones.fields import TimeZoneField

class Profile(models.Model):
    user = models.OneToOneField(User)
    skype = models.CharField("Skype ID", max_length=20, null=True, blank=True)
    aim = models.CharField("AIM", max_length=20, null=True, blank=True)
    gchat = models.CharField("Google Chat", max_length=20, null=True, blank=True)
    phone = models.CharField("Phone number", max_length=20, null=True, blank=True)
    is_available = models.BooleanField("Available now")
    timezone = TimeZoneField()

    skills = models.ManyToManyField('Skill', blank=True)
    def __unicode__(self):
        return unicode(self.user)

def create_profile_object(sender, instance, created, **kwargs):
    if not instance or not created:
        return
    Profile.objects.create(user=instance)
models.signals.post_save.connect(create_profile_object, sender=User)

class Skill(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
