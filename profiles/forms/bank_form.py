from django.forms import ModelForm
from django import forms
from profiles.models import *
from django.core.validators import MaxValueValidator


class CreateBankInfo(ModelForm):
    bank_nr = forms.IntegerField(required=True, label="Bank_number", help_text="Sláðu inn bankanúmer")
    ledger = forms.IntegerField(required=True, label="Ledger", help_text="Ledger")
    account_number = forms.IntegerField(required=True, label="Account_number", help_text="Account number")

    class Meta:
        model = UserBankInfo
        exclude = ['user']


class CreateUserBankInfo(ModelForm):
    card_nr = forms.CharField(required=True, label="Korta númer", help_text="Kortanúmer", max_length=16)
    exdate = forms.CharField(required=True, label="Útrennslu dagur", help_text="MM/YY", max_length=5)
    cvc = forms.IntegerField(required=True, label="CVC", help_text="CVC")

    class Meta:
        model = Card
        exclude = ['user']
