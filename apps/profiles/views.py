from django.views.generic.simple import direct_to_template
from profile.models import Profile
from profile.forms import SkillsForm

def SkillsTest(request):
    skills_form = SkillsForm()
    direct_to_template(request, 
                       'profiles/skills_test.html', 
                       {'skills_form':skills_form})
