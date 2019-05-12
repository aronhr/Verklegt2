from django import forms
from django.forms import ModelForm
from profiles.models import Profile, UserBankInfo
from django.contrib.auth.models import User


class ProfileForm(ModelForm):
    dob = forms.DateField(help_text='Sláðu inn færðingardag', label='Fæðingardagur', required=False)
    kt = forms.CharField(help_text='Sláðu inn kennitölu', label='Kennitala', required=False)
    address = forms.CharField(help_text='Sláðu inn heimilisfang', label='Heimilisfang', required=False)
    phone = forms.CharField(help_text='Sláðu inn símanúmer', label='Símanúmer', required=False)

    class Meta:
        model = Profile
        exclude = ['id', 'user', 'profile_pic']


class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'password', 'last_login', 'is_superuser', 'is_active', 'is_staff', 'date_joined', 'user_permissions', 'groups']


class BankForm(ModelForm):
    bank_nr = forms.CharField(label='Bankanúmer', help_text='Sláðu inn gilt bankanúmer', required=False, max_length=4)
    ledger = forms.CharField(label='Höfuðbók', help_text='Sláðu inn gilda höfuðbók', required=False, max_length=2)
    account_number = forms.CharField(label='Reikningsnúmer', help_text='Sláðu inn gilt reikningsnúmer', required=False, max_length=6)
    
    class Meta:
        model = UserBankInfo
        exclude = ['id', 'user']

