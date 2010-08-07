from models import Profile
from django import forms
from tagging.forms import TagField
from tagging_autocomplete.widgets import TagAutocomplete

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

class SkillsForm(forms.Form):
    skills = TagField(widget=TagAutocomplete())
