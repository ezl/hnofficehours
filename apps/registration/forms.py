import urllib2
from django import forms
from django.conf import settings


class RegistrationForm(forms.Form):
    hn_username = forms.CharField()

    def clean(self):
        hn_username = self.cleaned_data['hn_username']
        hn_profile_url = "http://news.ycombinator.com/user?id=%s" % hn_username
        hnoh_profile =  settings.USER_PROFILE_URL % hn_username
        page = urllib2.urlopen(hn_profile_url).read()
        if not hnoh_profile in page:
            raise forms.ValidationError('The url does not appear to be in your hn profile. Please paste %s into your hn profile. Note the trailing slash.' % hnoh_profile)
        return self.cleaned_data


