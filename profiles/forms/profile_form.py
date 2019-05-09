from django.forms import ModelForm
from profiles.models import Profile
from django.contrib.auth.models import User


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'kt', 'dob', 'user', 'profile_pic']


class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'password', 'last_login', 'is_superuser', 'is_active', 'is_staff', 'date_joined', 'user_permissions', 'groups']

