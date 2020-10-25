from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from register.models import Community, Manager


class CommunityAdmin(admin.ModelAdmin):
    fields = ['name', 'city', 'description', 'telegram', 'logo']

class ManagerInline(admin.StackedInline):
    model = Manager
    can_delete = False
    verbose_name = 'Community Manager'

class UserAdmin(BaseUserAdmin):
    inlines = (ManagerInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

admin.site.register(Community, CommunityAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)