from datetime import datetime, timedelta
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic.simple import direct_to_template
from schedule.models import Event


def site_index(request, template_name='index.html'):
    def _format_office_hour(office_hour):
        # get the office hour holder, skills, contact methods
        return office_hour
    events = Event.objects.all()
    start = datetime.now()
    end = start + timedelta(days=7)
    office_hours = reduce(lambda x,y: x+y, [e.get_occurrences(start, end)
                                            for e in events]) if events else []
    office_hours = map(_format_office_hour, office_hours)
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

def about(request):
    return direct_to_template(request, 'about.html')
