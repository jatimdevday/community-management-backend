from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic.edit import CreateView
from register.forms import CommunityForm, ManagerForm

# Create your views here.
class CommunityCreate(CreateView):
    form_class = CommunityForm
    template_name = 'register_community.html'


class ManagerCreate(CreateView):
    form_class = ManagerForm
    template_name = 'register_manager.html'