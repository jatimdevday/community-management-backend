"""
Basic views for backend_jdd
"""

# from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from social_django.models import UserSocialAuth

"""Home view for user after login"""
@login_required
def home(request):
    # display username
    username = request.user.username if request.user.username else 'Guest'
    # display userdata, could be used for multiple auth. see https://github.com/Alexmhack/django_oauth
    extra_data = ''

    try:
        extra_data += '</br> Github : ' + str(request.user.social_auth.get(provider='github').extra_data)
    except UserSocialAuth.DoesNotExist:
        extra_data += '</br> Github account not set. <a href="http://127.0.0.1:8000/social-auth/login/github/">Login with Github</a>'
        
    try:
        extra_data += '</br> Google : ' + str(request.user.social_auth.get(provider='google-oauth2').extra_data)
    except UserSocialAuth.DoesNotExist:
        extra_data += '</br> Google account not set. <a href="http://127.0.0.1:8000/social-auth/login/google-oauth2/">Login with Google</a>'
        
    return HttpResponse('Halo {} \n {}'.format(username, extra_data))

def login(request):
    # using template : ... href={% url 'social:begin' 'github' %} ...
    display_str = '''
             <a href="http://127.0.0.1:8000/social-auth/login/github/">Login with Github</a>
        </br><a href="http://127.0.0.1:8000/social-auth/login/google-oauth2/">Login with Google</a>
        '''

    return HttpResponse(display_str) 