import calendar
from django.conf import settings
from django import forms
from django.utils.translation import ugettext_lazy as _
from schedule.forms import *
from schedule.models import Event


# If we ever go international, FIRST_DAY_OF_WEEK needs to be a user setting.
# See Calendar.firstweekday() in python ``calendar`` module for more info.
FIRST_DAY_OF_WEEK = getattr(settings, 'FIRST_DAY_OF_WEEK', 0)
# WEEKDAY_CHOICES = [(i % 7, calendar.day_name[i % 7]) for i in range(FIRST_DAY_OF_WEEK, FIRST_DAY_OF_WEEK+7)]
WEEKDAY_CHOICES = [(i % 7, calendar.day_name[i % 7]) for i in range(0, 7)]

class EventForm(SpanForm):
    repeats = forms.BooleanField(required=False)
    end_recurring_period = forms.DateTimeField(label="Repeats until",
                                               required=False,
                                               help_text = _("This date is ignored for one-time-only events."))
    repeats_on = forms.MultipleChoiceField(choices=WEEKDAY_CHOICES,
                                           required=False,
                                           widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Event
        fields = ('start', 'end', 'repeats', 'end_recurring_period',
                  'repeats_on',)

    def __init__(self, hour24=False, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

    def clean(self):
        if self.cleaned_data.get('repeats', False):
            if len(self.cleaned_data.get('repeats_on', [])) == 0:
                raise forms.ValidationError("If the events repeats, you must specific on which weekdays it repeats.")
        return self.cleaned_data
