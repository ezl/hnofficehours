from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
import schedule.models
from schedule.models import Calendar


def create_global_calendar(sender=None, app=None, **kwargs):
    if not sender:
        return
    cal_name = getattr(settings, 'GLOBAL_CALENDAR_SLUG', 'cal')
    Calendar.objects.get_or_create_calendar_for_object(Site.objects.get_current(),
                                                       name=cal_name)
models.signals.post_syncdb.connect(create_global_calendar, sender=schedule.models)
