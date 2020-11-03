from django.db import models
from datetime import MAXYEAR, datetime, timedelta
from django.utils.timezone import make_aware, get_default_timezone, now
from django.core.exceptions import ValidationError


class EventQuerySet(models.QuerySet):
    # published_at < now
    def published(self):
        return self.filter(published_at__lt=now())

    # NOT published_at < now
    def draft(self):
        return self.exclude(published_at__lt=now())


class EventManager(models.Manager):
    def get_queryset(self):
        return EventQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def draft(self):
        return self.get_queryset().draft()


class Event(models.Model):
    # model properties 
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    start_at = models.DateTimeField(blank=False)
    end_at = models.DateTimeField(blank=False)
    created_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=datetime(MAXYEAR, 12, 31, 23, 59, 59, 999999, tzinfo=get_default_timezone())) # set default as 'drafts'
    # community_organizer #TBA
    # image_url #TBA

    # model meta
    class Meta:
        ordering = ['start_at', 'published_at']

    # model manager
    objects = EventManager()

    # override save method
    def save(self, *args, **kwargs):
        if self.end_at < self.start_at:
            raise ValidationError("End date happen before start date.")

        super().save(*args, **kwargs) # actual save

    def __str__(self):
        return self.title

