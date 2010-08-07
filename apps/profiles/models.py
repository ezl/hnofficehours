from django.db import models
from django.contrib.auth.models import User
from tagging.fields import TagField
from tagging.models import Tag
from tagging_autocomplete.models import TagAutocompleteField

class Profile(models.Model):
    user = models.OneToOneField(User)
    skills = TagAutocompleteField()
    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self, tags):
        return Tags.objects.get_for_object(self)
