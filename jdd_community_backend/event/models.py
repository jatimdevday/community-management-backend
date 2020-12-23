from django.db import models
from datetime import MAXYEAR, datetime, timedelta
from django.utils.timezone import make_aware, get_default_timezone, now
from django.core.exceptions import ValidationError

class EventQuerySet(models.QuerySet):
    # published_at < now
    def published(self):
        return self.filter(is_published=True)

    # NOT published_at < now
    def draft(self):
        return self.filter(is_published=False)
"""
    # started at between 2 date
    def start_between(self, from_date, to_date):
        return self.filter(start_at__range=[from_date, to_date])
"""

class EventManager(models.Manager):
    def get_queryset(self, query=None):
        return EventQuerySet(self.model, query=query, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def draft(self):
        return self.get_queryset().draft()
"""
    def start_between(self, from_date, to_date):
        return self.get_queryset(query=[from_date,to_date])
"""

class Event(models.Model):
    # model properties 
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    start_at = models.DateTimeField(blank=False)
    end_at = models.DateTimeField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    # updated_at = models.DateTimeField(auto_now=True) # subject to change
    # community_organizer #TBA #TODO impl as FK
    # image_url #TBA
    # tags
    # location
    # ...
    # after_event_url

    # model meta
    class Meta:
        ordering = ['start_at', 'is_published']

    # model manager
    objects = EventManager()

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})

    # override save method
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs) # actual save

    # override clean method
    def clean(self):
        super().clean()
        if self.end_at < self.start_at:
            raise ValidationError("End date happen before start date.")

    def __str__(self):
        return self.title

