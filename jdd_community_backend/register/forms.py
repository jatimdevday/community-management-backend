from django.forms import ModelForm, ModelChoiceField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from register.models import Community, Manager


class CommunityForm(ModelForm):
    class Meta:
        model = Community
        fields = ['name', 'city', 'description', 'telegram', 'logo']


class ManagerForm(ModelForm):
    community = ModelChoiceField(queryset=Community.objects.all(),
                                to_field_name = 'name',
                                empty_label="Select Community")

    class Meta:
        model = Manager
        fields = ['picture', 'community']


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name") 