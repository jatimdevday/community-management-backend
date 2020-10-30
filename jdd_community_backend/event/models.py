from django.db import models


class Event(models.Model):
    published = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    # community_organizer = #ASK use on this model or use 1to1?

    class Meta:
        ordering = ['start_date', 'published']

    def __str__(self):
        return self.title

