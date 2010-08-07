import urllib2
from django import forms
from django.conf import settings
from retrieve_hn_user_data import retrieve_hn_user_data
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):
    hn_username = forms.CharField()

    def clean(self):
        hn_username = self.cleaned_data['hn_username']
        hnoh_profile =  settings.USER_PROFILE_URL % hn_username
        try:
            user_data = retrieve_hn_user_data(hn_username)
        except:
            errormsg = "%s does not appear to be a registered HN username" % hn_username
            raise forms.ValidationError(errormsg)
            print "adsfhaldfadsf"
        if not hnoh_profile in user_data["about"]:
            raise forms.ValidationError('The url does not appear to be in your hn profile. Please paste %s into your hn profile. Note the trailing slash.' % hnoh_profile)
        if User.objects.filter(username=hn_username).count() > 0:
            errormsg = 'User "%s" already has an account' % hn_username
            raise forms.ValidationError(errormsg)
        return self.cleaned_data
