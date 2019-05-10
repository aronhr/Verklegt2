from django.forms import ModelForm
from house.models import House, HouseInfo, HouseImage
from django import forms


class PropCreateForm(ModelForm):
    address = forms.CharField(required=True, label='Heimilisfang', help_text='Sláðu inn heimilisfang án húsnúmers')
    street_nr = forms.CharField(required=True, label='Húsnúmer', help_text='Sláðu inn húsnúmer')
    price = forms.IntegerField(required=True, label='Verð á húsnæði', help_text='Sláðu inn verð á húsnæði')
    p_code = forms.Select()

    class Meta:
        model = House
        exclude = ['id', 'seller', 'on_sale', 'sellingdate']


class CreateHouseInfo(ModelForm):
    description = forms.CharField(required=True, label="Lýsing", help_text='Sláðu inn lýsingu')
    rooms = forms.IntegerField(required=True, label="Herbergi", help_text='Sláðu inn fjölda herbergja')
    buildyear = forms.IntegerField(required=True, label="Byggingaár", help_text='Sláðu inn ár sem fasteignin var byggð')
    size = forms.IntegerField(required=True, label='Stærð', help_text='Sláðu inn stærð í fermetrum')
    garage = forms.BooleanField(label='Bílskúr')
    extra_apartment = forms.BooleanField(label='Auka íbúð')
    elevator = forms.BooleanField(label='Lyfta')
    entrance = forms.BooleanField(label='Séringangur')
    new_building = forms.BooleanField(label='Ný Bygging')

    class Meta:
        model = HouseInfo
        exclude = ['id', 'house']
