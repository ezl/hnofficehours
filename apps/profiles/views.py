from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.simple import direct_to_template

from profiles.models import *
from profiles.forms import ProfileForm, ProfileSkillsForm
from django.contrib.auth.decorators import login_required

def userprofile(request, username=None, template_name='profiles/profile.html'):
    form = ProfileForm()
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

def ajax_view(request, profile_id, skill_id, verb):
    profile = Profile.objects.get(id = profile_id)
    skill = Skill.objects.get(id = skill_id)
    if verb == "remove":
        profile.skills.remove(skill)
        return HttpResponse("success")
    else:
        return HttpResponse("verb unrecognized")

#@login_required
def profile(request):
    user = request.user
    profile = user.profile
    if request.method == "POST":
        tag_list = request.POST.get('skills_text').strip(',').split(' ')
        for tag in tag_list:
            if tag and tag != '':
                skill, created = Skill.objects.get_or_create(name=tag)
                profile.skills.add(skill)
        psf = ProfileSkillsForm(request.POST)
        if psf.is_valid():
            skills_list = Skill.objects.filter(id__in = psf.cleaned_data.get('skills'))
            for skill in skills_list:
                profile.skills.add(skill)
        profile.save()
    profile_form = ProfileSkillsForm()
    skills = profile.skills.all()
    return direct_to_template(request, 'profiles/skills_test.html', 
                                        {'profile_form':profile_form,
                                         'profile':profile,
                                         'skills':skills})
