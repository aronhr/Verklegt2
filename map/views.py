from django.shortcuts import render
from house.models import House
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my-application")


def index(request):
    geo = {"houses": []}
    for x in House.objects.all():
        try:
            location = geolocator.geocode(x.address + " " + x.street_nr)
            geo["houses"].append({'id': x.id, 'geo': {'lat': location.latitude, 'lng': location.longitude}, 'address': x.address + ' ' + x.street_nr, 'image': x.houseimage_set.first})
        except:
            continue
    return render(request, 'map/index.html', geo)
