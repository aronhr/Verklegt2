from django.forms import ModelForm
from django import forms
from profiles.models import *


class CreateUserBankInfo(ModelForm):
    card_nr = forms.CharField(required=True, label="Kortanúmer", help_text="Kortanúmer", max_length=20)
    exdate = forms.CharField(required=True, label="Gildistími", help_text="MM/YY", max_length=5)
    cvc = forms.IntegerField(required=True, label="Öryggisnúmer", help_text="Öryggisnúmer")

    class Meta:
        model = Card
        exclude = ['user']
