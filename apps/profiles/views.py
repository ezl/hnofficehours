from django.views.generic.simple import direct_to_template
from profiles.models import Profile
from profiles.forms import SkillsForm

def skills_test(request):
    skills_form = SkillsForm()
    return direct_to_template(request, 'profiles/skills_test.html', 
                       				  {'skills_form':skills_form})
