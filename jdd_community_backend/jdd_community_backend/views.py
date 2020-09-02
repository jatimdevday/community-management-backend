"""
Basic views for backend_jdd
"""

# from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

"""Home view for user after login"""
@login_required
def home(request):
    s = request.user.username if request.user.username else "Guest"
    return HttpResponse("Halo {} \n {}".format(s, request.user.social_auth.get(provider='github').extra_data))

def login(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/social-auth/login/github/">Login with Github</a>') 