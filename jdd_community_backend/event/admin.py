from django.contrib import admin
from event.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_at', 'end_at']

# add to admin panel
admin.site.register(Event, EventAdmin)