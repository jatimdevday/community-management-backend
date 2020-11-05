from django import forms
from datetime import datetime
from django.utils.timezone import now
from event.models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_at', 'end_at']
        widgets = {
           'start_at': forms.DateTimeInput(format=('%m/%d/%Y %H:%M:%S'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'datetime-local'}),
           'end_at': forms.DateTimeInput(format=('%m/%d/%Y %H:%M:%S'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'datetime-local'}),
        }

    