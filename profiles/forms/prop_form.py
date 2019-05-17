from django.forms import ModelForm
from house.models import House, HouseInfo, HouseImage, PostalCodes
from django import forms



class PropCreateForm(ModelForm):
    address = forms.CharField(required=True, label='Heimilisfang', help_text='Sláðu inn heimilisfang án húsnúmers')
    street_nr = forms.CharField(required=True, label='Húsnúmer', help_text='Sláðu inn húsnúmer')
    price = forms.IntegerField(required=True, label='Verð á húsnæði', help_text='Sláðu inn verð á húsnæði')
    p_code = forms.Select()

    class Meta:
        model = House
        exclude = ['id', 'seller', 'on_sale', 'sellingdate']

    def __init__(self, *args, **kwargs):
        super(PropCreateForm, self).__init__(*args, **kwargs)
        self.fields['p_code'].queryset = PostalCodes.objects.order_by('id')


class CreateHouseInfo(ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea', ' data-length': 1500}), required=True, label="Lýsing", help_text='Sláðu inn lýsingu')
    rooms = forms.IntegerField(required=True, label="Herbergi", help_text='Sláðu inn fjölda herbergja')
    buildyear = forms.IntegerField(required=True, label="Byggingaár", help_text='Sláðu inn ár sem fasteignin var byggð')
    size = forms.IntegerField(required=True, label='Stærð', help_text='Sláðu inn stærð í fermetrum')
    garage = forms.BooleanField(required=False, label='Bílskúr')
    extra_apartment = forms.BooleanField(required=False, label='Auka íbúð')
    elevator = forms.BooleanField(required=False, label='Lyfta')
    entrance = forms.BooleanField(required=False, label='Séringangur')
    new_building = forms.BooleanField(required=False, label='Ný Bygging')

    class Meta:
        model = HouseInfo
        exclude = ['id', 'house']
