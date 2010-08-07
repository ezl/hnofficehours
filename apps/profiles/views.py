from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.simple import direct_to_template

from profiles.models import Profile
from profiles.forms import SkillsForm, ProfileForm


def skills_test(request):
    skills_form = SkillsForm()
    return direct_to_template(request, 'profiles/skills_test.html',
                              {'skills_form':skills_form})

def userprofile(request, username=None, template_name='profiles/profile.html'):
    form = ProfileForm()
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

