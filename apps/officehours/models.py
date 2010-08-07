from django.contrib.auth.models import User
from django.db import models
from django.db.models import signals
from schedule.models import Calendar


def create_user_calendar(sender, instance=None, **kwargs):
    """
    Whenever a User object is created/saved, make sure there's Calendar
    object associated with that User. The django-schedule looks up calendars
    by slug, so just make the slug the User's username.
    """
    if not instance:
        return
    cal = Calendar.objects.get_or_create_calendar_for_object(instance,
                                                         name=instance.username)
signals.post_save.connect(create_user_calendar, sender=User)
