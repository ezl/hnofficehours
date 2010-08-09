import sys
from django.db import models


class LastUpdate(models.Model):
    """
    Just need a convenient place to store the last time the update_availability
    task ran so that we can define a Period object for the appropriate time
    delta.
    """
    last_update = models.DateTimeField(null=True, auto_now=True)

    def __unicode__(self):
        return str(self.last_update)


def set_first_update(sender=None, app=None, **kwargs):
    if not sender:
        return
    LastUpdate.objects.create()
this_module = sys.modules[globals()['__name__']]
models.signals.post_syncdb.connect(set_first_update, sender=this_module)
