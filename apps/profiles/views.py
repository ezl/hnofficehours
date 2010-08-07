from django.views.generic.simple import direct_to_template
from profiles.models import Profile
from profiles.forms import ProfileForm, ProfileSkillsForm
from django.contrib.auth.decorators import login_required

#@login_required
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
