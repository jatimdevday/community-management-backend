from django.contrib import admin
from event.models import Event
from . import forms

class EventAdmin(admin.ModelAdmin):
    # use django form
    form = forms.EventForm

    # how it looks like in admin
    list_display = ['title', 'start_at', 'end_at']
    list_filter = ['start_at', 'end_at', 'is_published']
    date_hierarchy='start_at'
    ordering=['-start_at']

# add to admin panel
admin.site.register(Event, EventAdmin)