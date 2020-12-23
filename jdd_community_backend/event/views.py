from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from event.models import Event
from event.forms import EventForm


class EventEndpoint(View):
    def post(self, request):
        f = EventForm(request.POST)
        if f.is_valid():
            new_event = f.save(commit=False)
            new_event.is_published = True # override default behaviour
            new_event.save()
        # return HttpResponse('Saved {}'.format(str(new_event)))
        return redirect('event')

    def get(self, request):
        latest_events = Event.objects.all()
        # latest_events = Event.objects.published()[:5]
        output = '<br>'.join(['{} :: {} -sd- {}'.format(e.title, e.start_at, e.end_at) for e in latest_events])
        return HttpResponse(output)

    def put(self, request):
        pass # not yet implemented

    def delete(self, request):
        pass # not yet implemented


class EventCreate(CreateView):
    template_name = 'event/create.html'
    form_class = EventForm
    success_url = 'event/'        

# not yet implemented
"""    
class EventList(ListView):
    template_name = 'event/list.html'
    model = Event

class EventDetail(DetailView):
    template_name = 'event/detail.html'
    model = Event

class EventUpdate(UpdateView):
    template_name = 'event/update.html'
    model = Event
    fields = ['title', 'description', 'start_at', 'end_at']

class EventDelete(DeleteView):
template_name = 'event/delete.html'
    model = Event
    success_url = reverse_lazy('event')

"""
