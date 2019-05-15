from django.forms import ModelForm
from house.models import Offers
from django import forms


class OfferForm(ModelForm):
    price = forms.IntegerField(required=True, label="Verð", help_text="Sláðu inn upphæð")

    class Meta:
        model = Offers
        exclude = ['user', 'seller', 'house', 'date', 'state', 'seen']
