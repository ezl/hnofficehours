from django.conf import settings

def output_timezone(request):
    tz = request.user.get_profile().timezone if request.user.is_authenticated()\
            else settings.TIME_ZONE
    return {'output_timezone':  tz}
