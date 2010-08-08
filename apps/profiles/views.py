from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic.simple import direct_to_template
from schedule.models import Event

from profiles.models import Profile
from profiles.forms import ProfileForm, ProfileSkillsForm
from django.contrib.auth.decorators import login_required


def _can_view_full_profile(user):
    # for now just check if user is logged in, later there may be karma and/or
    # other requirements.
    return user.is_authenticated()

def list_profiles(request, template_name='profiles/list_profiles.html'):
    users = User.objects.all()
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

def view_profile(request, username, template_name='profiles/view_profile.html'):
    user = get_object_or_404(User, username=username)
    display_full_profile = _can_view_full_profile(request.user)
    events = Event.objects.filter(creator=user)
    start = datetime.now()
    end = start + timedelta(days=7)
    office_hours = reduce(lambda x,y: x+y, [e.get_occurrences(start, end)
                                            for e in events]) if events else []
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))


@login_required
def profile(request):
    if request.method == "POST":
        #import ipdb; ipdb.set_trace()
        tag_list = request.POST.get('skills_text').strip(',').split(' ')
        for tag in tag_list:
            skill, created = Skill.objects.get_or_create(name=name)
    else:
        profile_form = ProfileSkillsForm()
    return direct_to_template(request, 'profiles/skills_test.html', 
                                        {'profile_form':profile_form})
