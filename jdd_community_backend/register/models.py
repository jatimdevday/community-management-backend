from django.db import models
from django.urls import reverse

# Create your models here.
class Community(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='community-logo')
    telegram = models.CharField(max_length=100)

    def get_absolute_url(self): # new
        return reverse('register-community')
    
    def __str__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    picture = models.ImageField(upload_to='manager-picture')
    community = models.ForeignKey(
        Community,
        on_delete=models.CASCADE,
    )

    def get_absolute_url(self): # new
        return reverse('register-manager')