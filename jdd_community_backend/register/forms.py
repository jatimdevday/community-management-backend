from register.models import Community, Manager
from django.forms import ModelForm, ModelChoiceField


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
        fields = ['name', 'email', 'picture', 'community']