from django.forms import ModelForm, widgets
from profiles.models import Profile

"""
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'first_name': widgets.TextInput(attrs='input-field'),
            'last_name': widgets.TextInput(attrs='input-field'),
            'username': widgets.TextInput(attrs='input-field'),
            'email': widgets.EmailInput(attrs='input-field'),
            'kt': widgets.TextInput(attrs='input-field'),
            'phone': widgets.NumberInput(attrs='input-field'),
            'address': widgets.TextInput(attrs='input-field'),
        }
"""

