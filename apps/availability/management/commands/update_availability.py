from django.core.management.base import NoArgsCommand
from schedule.models import Event
from schedule.periods import Period


class Command(NoArgsCommand):
    help = 'Update `available` flag for every user whose office hours changed since last check.'

    def handle_noargs(self, **options):
        print "hello world"
        now = Period(events=events, start=datetime.now(),
                                end=datetime.now() + timedelta(minutes=1))
        occurrences = now.get_occurrences_partials()
        print(occurrences)
        print "goodbye cruel world"
