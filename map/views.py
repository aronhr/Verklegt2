from django.shortcuts import render
from house.models import House
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my-application")

#print(location.address)
#print((location.latitude, location.longitude))


# Create your views here.
def index(request):
    geo = []
    for x in House.objects.all():
        try:
            print(x.address + " " + x.street_nr)
            location = geolocator.geocode(x.address + " " + x.street_nr)
            print((location.latitude, location.longitude))
            #geo.append(f"{{lat: {location.latitude}, lng: {location.longitude}}},")
            geo.append(["Linkur", location.latitude, location.longitude, x.address + " " + x.street_nr])
        except:
            pass
    # geo[-1] = geo[-1][:-1]
    return render(request, 'map/index.html', {
        'map': 'this is a cool map u know',
        'ad': geo
    })