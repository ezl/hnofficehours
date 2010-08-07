from django.views.generic.simple import direct_to_template
from profiles.models import Profile
from profiles.forms import ProfileForm

def skills_test(request):
    profile_form = ProfileForm()
    return direct_to_template(request, 'profiles/skills_test.html', 
                       				  {'profile_form':profile_form})
