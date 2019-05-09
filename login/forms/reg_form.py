from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='Skírnafn', help_text='Settu inn skírnafn')
    last_name = forms.CharField(label='Eftirnafn', help_text='Settu inn eftirnafn')
    email = forms.EmailField(label='Netfang', help_text='Settu inn netfang')
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
