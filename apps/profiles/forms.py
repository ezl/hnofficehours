from django import forms
from tagging.forms import TagField
from tagging_autocomplete.widgets import TagAutocomplete
from profiles.models import *

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
