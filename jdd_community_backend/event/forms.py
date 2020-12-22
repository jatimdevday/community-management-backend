
from datetime import datetime
from django.utils.timezone import now
from django import forms
from jdd_community_backend.settings import base as base_setting
from event.models import Event


class EventForm(forms.ModelForm):
    
    # more definitions
    start_at = forms.DateTimeField(input_formats=(base_setting.DATETIME_INPUT_FORMATS),
                                    widget=forms.DateTimeInput(format=base_setting.DATETIME_INPUT_FORMATS, attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'datetime-local'}), 
                                )
    end_at = forms.DateTimeField(input_formats=(base_setting.DATETIME_INPUT_FORMATS),
                                    widget=forms.DateTimeInput(format=base_setting.DATETIME_INPUT_FORMATS, attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'datetime-local'}), 
                                )
    is_published = forms.BooleanField(required=False)

    class Meta:
        model = Event
        fields = ['title', 'description', 'start_at', 'end_at', 'is_published']
    
    

    