from django.shortcuts import render
from house.models import *
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my-application", format_string="%s, Iceland")


def index(request):
    geo = {"houses": []}
    for house in House.objects.all():
        try:
            location = geolocator.geocode(house.address + " " + house.street_nr + ", " + str(house.p_code))
            geo["houses"].append({'id': house.id, 'geo': {'lat': location.latitude, 'lng': location.longitude},
                                  'address': house.address + ' ' + house.street_nr, 'image': house.houseimage_set.first,
                                  'description': house.houseinfo_set.first})
        except:
            continue
    return render(request, 'map/index.html', geo)
