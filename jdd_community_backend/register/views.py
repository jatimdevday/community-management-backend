from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from register.forms import CommunityForm, ManagerForm, UserForm

# Create your views here.
class CommunityCreateView(CreateView):
    form_class = CommunityForm
    template_name = 'register_community.html'


def create_manager(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        manager_form = ManagerForm(request.POST, request.FILES)
        print(manager_form.is_valid())
        print(request.POST)
        if user_form.is_valid() and manager_form.is_valid():
            user = user_form.save()
            manager = manager_form.save(commit=False)
            manager.user = user
            manager.save()
            return redirect('register-manager')
    else:
        user_form = UserForm()
        manager_form = ManagerForm()
    return render(
        request,
        'register_manager.html',
        {'user_form': user_form, 'manager_form': manager_form}
    ) 