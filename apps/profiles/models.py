from django.db import models
from django.contrib.auth.models import User
from tagging.fields import TagField
from tagging.models import Tag
from timezones.fields import TimeZoneField


class Profile(models.Model):
    user = models.OneToOneField(User)
    skype = models.CharField("Skype ID", max_length=20, null=True, blank=True)
    aim = models.CharField("AIM", max_length=20, null=True, blank=True)
    gchat = models.CharField("Google Chat", max_length=20, null=True, blank=True)
    phone = models.CharField("Phone number", max_length=20, null=True, blank=True)
    timezone = TimeZoneField()

    skills = TagField()
    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self, tags):
        return Tags.objects.get_for_object(self)
