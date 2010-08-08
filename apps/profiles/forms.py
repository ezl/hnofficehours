from models import Profile
from django import forms
from tagging.forms import TagField
from tagging_autocomplete.widgets import TagAutocomplete
from profiles.models import *
from ajax_select.fields import AutoCompleteSelectMultipleField, AutoCompleteSelectField

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('skype', 'aim', 'gchat', 'phone', 'timezone')

class ProfileSkillsForm(forms.Form):
    # declare a field and specify the named channel that it uses
    skills = AutoCompleteSelectMultipleField('profile_skills', required=False)
