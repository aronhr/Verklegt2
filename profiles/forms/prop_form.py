from django.forms import ModelForm, widgets
from house.models import House, HouseInfo, HouseType
from django import forms


class PropCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input-field'}))
    address = forms.CharField(required=True, label='Heimilisfang', help_text='Sláðu inn heimilisfang án húsnúmers')
    street_nr = forms.CharField(required=True, label='Húsnúmer', help_text='Sláðu inn húsnúmer')
    price = forms.IntegerField(required=True, label='Verð á húsnæði', help_text='Sláðu inn verð á húsnæði')
    p_code = forms.Select()
    sellingdate = forms.DateField(required=True, label='Söludagsetning')

    class Meta:
        model = House
        exclude = ['id', 'seller', 'on_sale']


class CreateHouseInfo(ModelForm):
    description = forms.CharField(required=True, label="Lýsing", help_text='Sláðu inn lýsingu', widget=forms.Textarea)
    rooms = forms.Select()
    buildyear = forms.IntegerField(required=True, label="Byggingaár", help_text='Sláðu inn ár sem fasteignin var byggð')

    class Meta:
        model = HouseInfo
        exclude = ['id', 'house', 'type', 'garage', 'extra_apartment', 'elevator', 'entrance']


class CheckBoxForm(ModelForm):
    garage = forms.BooleanField(label='Bílskúr')
    extra_apartment = forms.BooleanField(label='Auka íbúð')
    elevator = forms.BooleanField(label='Lyfta')
    entrance = forms.BooleanField(label='Séringangur')

    class Meta:
        model = HouseInfo
        exclude = ['id', 'house', 'type', 'description', 'rooms', 'buildyear']


class CreateHouseType(ModelForm):

    class Meta:
        model = HouseType
        exclude = ['id']
        widgets = {
            'type': widgets.Select(attrs={'class': 'input-field'})
        }
