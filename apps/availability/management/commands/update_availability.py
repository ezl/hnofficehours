from django.core.management.base import NoArgsCommand
from availability.models import LastUpdate
from schedule.models import Event
from schedule.periods import Period


class Command(NoArgsCommand):
    """
    DOCTEST GOES HERE :-P
    """
    help = 'Update `available` flag for every user whose office hours changed since last check.'

    def handle_noargs(self, **options):
        print "starting"
        last_update = LastUpdate.objects.all()[0].when
        now = datetime.now()
        delta = Period(events=events, start=last_update, end=now)
        print(delta)
        partials = delta.get_occurrences_partials()
        # ccg left off here.
        # from get_occurrences_partials() docs:
        # "Each element in the returned list is a dictionary {'event': event, 'class': 0}"
        # relevant partial classes:
        # class 0: The event begins in this period
        # class 3: The event ends during this period
        for partial in partials:
            if partial['class'] == 1:
                pass    # partial->event->owner->available=True
            elif partial['class'] == 3:
                pass    # partial->event->owner->available=False
        print(occurrences)
        last_update.save()  # automatically updates its own timestamp
        print "stopping"
