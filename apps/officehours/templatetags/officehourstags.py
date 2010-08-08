from django import template
from django.core.urlresolvers import reverse
from schedule.templatetags.scheduletags import *

register = template.Library()

@register.simple_tag
def prev_url(target, period):
    return '%s%s' % (
        reverse(target),
            querystring_for_date(period.prev().start))

@register.simple_tag
def next_url(target, period):
    return '%s%s' % (
        reverse(target),
            querystring_for_date(period.next().start))

@register.inclusion_tag("schedule/_create_event_options.html", takes_context=True)
def create_event_url(context, calendar, slot ):
    context.update ( {
        'calendar' : calendar,
        'MEDIA_URL' : getattr(settings, "MEDIA_URL"),
    })
    # lookup_context = {
    #     'calendar_slug': calendar.slug,
    # }
    context['create_event_url'] ="%s%s" % (
        reverse("calendar_create_event"),
        querystring_for_date(slot))
    return context


@register.inclusion_tag("schedule/_event_options.html", takes_context=True)
def options(context, occurrence ):
    context.update({
        'occurrence' : occurrence,
        'MEDIA_URL' : getattr(settings, "MEDIA_URL"),                                                        
    })
    context['view_occurrence'] = occurrence.get_absolute_url()
    user = context['request'].user
    if CHECK_PERMISSION_FUNC(occurrence.event, user):
        context['edit_occurrence'] = occurrence.get_edit_url()
        print context['edit_occurrence']
        context['cancel_occurrence'] = occurrence.get_cancel_url()
        context['delete_event'] = reverse('delete_event', args=(occurrence.event.id,))
        context['edit_event'] = reverse('edit_event', args=(occurrence.event.id,))
    else:
        context['edit_event'] = context['delete_event'] = ''
    return context