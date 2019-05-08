from django.forms import ModelForm, widgets
from house.models import House
from django import forms


class PropCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input-field'}))

    class Meta:
        model = House
        exclude = ['id']
        widgets = {
            'address': widgets.TextInput(attrs={'class': 'input-field'}),
            'street_nr': widgets.NumberInput(attrs={'class': 'input-field'}),
            'price': widgets.NumberInput(attrs={'class': 'input-field'}),
            'p_code': widgets.NumberInput(attrs={'class': 'input-field'}),
            'seller': widgets.NumberInput(attrs={'class': 'input-field'}),
            'on_sale': widgets.CheckboxInput(attrs={'class': 'input-field'}),
            'sellingdate': widgets.DateInput(attrs={'class': 'datepicker'}),
        }
