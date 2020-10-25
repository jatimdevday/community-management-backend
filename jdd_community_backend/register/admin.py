from django.contrib import admin

# Register your models here.
from django.contrib import admin

from register.models import Community, Manager


class CommunityAdmin(admin.ModelAdmin):
    fields = ['name', 'city', 'description', 'telegram', 'logo']


class ManagerAdmin(admin.ModelAdmin):
    fields = ['user', 'picture', 'community']

admin.site.register(Community, CommunityAdmin)
admin.site.register(Manager, ManagerAdmin)