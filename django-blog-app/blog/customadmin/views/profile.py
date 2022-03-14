from django.shortcuts import render , redirect , reverse
from .generic import MyCreateView,MyDeleteView, MyListView,MyUpdateView,MyDetailView
from ..models import Profile
from ..forms import ProfileUpdateForm

class ProfileListView(MyListView):
    model = Profile
    template_name = 'customadmin/profile/profile_list.html'
    context_object_name = 'profile'

class ProfileDetailView(MyDetailView):
    model = Profile
    template_name = 'customadmin/profile/profile_detail.html'
    context_object_name = "profile"

class ProfileUpdateView(MyUpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'customadmin/profile/profile_update.html'

    def get_success_url(self):
        return reverse('customadmin:profile-list')


class ProfileDeleteView(MyDeleteView):
    model = Profile
    template_name = 'customadmin/confirm_delete.html'

    def get_success_url(self):
        return reverse('customadmin:profile-list')