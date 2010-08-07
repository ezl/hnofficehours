from django import forms
from tagging.forms import TagField
from tagging_autocomplete.widgets import TagAutocomplete

class TestTags(forms.Form):
    skills = TagField(widget=TagAutocomplete())
