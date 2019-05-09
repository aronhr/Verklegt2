from django.forms import ModelForm, widgets
from house.models import House, HouseInfo, HouseType
from django import forms


class PropCreateForm(ModelForm):
    description = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input-field'}))
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input-field'}))

    class Meta:
        model = House
        exclude = ['id', 'seller', 'on_sale']
        widgets = {
            'address': widgets.TextInput(attrs={'class': 'input-field'}),
            'street_nr': widgets.NumberInput(attrs={'class': 'input-field'}),
            'price': widgets.NumberInput(attrs={'class': 'input-field'}),
            'p_code': widgets.Select(attrs={'class': 'input-field'}),
            'sellingdate': widgets.DateInput(attrs={'class': 'datepicker'}),
        }


class CreateHouseInfo(ModelForm):

    class Meta:
        model = HouseInfo
        exclude = ['id', 'house', 'type']
        widgets = {
            'description': widgets.TextInput(attrs={'class': 'input-field'}),
            'rooms': widgets.NumberInput(attrs={'class': 'input-field'}),
            'size': widgets.NumberInput(attrs={'class': 'input-field'}),
            'garage': widgets.CheckboxInput(attrs={'class': 'input-field'}),
            'extra_apartment': widgets.CheckboxInput(attrs={'class': 'input-field'}),
            'elevator': widgets.CheckboxInput(attrs={'class': 'input-field'}),
            'entrance': widgets.CheckboxInput(attrs={'class': 'input-field'}),
            'buildyear': widgets.NumberInput(attrs={'class': 'input-field'})
        }
