from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from house.models import *
from profiles.models import User


def index(request):
    p = HouseInfo.objects.all()
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        houses = [{
            'type': x.type,
            #Þarf að fá upplýsingar um bæði houseInfo og house.. því ég leitae eftir mismundani upplýsingum.
            #for x in House.objects.filter(room=search_filter)
        } for x in HouseInfo.objects.filter(type=search_filter)]
        return JsonResponse({'data': houses})
        #Þarf að laga hvað er í gangi herna
    context = {
        'houses': House.objects.all(),
        'house_info': HouseInfo.objects.all(),
        'types': HouseType.objects.all(),
        'towns': PostalCodes.objects.all(),
        'postal_codes': request.POST.getlist('postal_codes'),
        'lyfta': request.POST.get('lyfta'),
        'rooms': request.POST.get('rooms')
        }

    print(str(p[0].id) in request.POST.getlist('postal_codes'))
    print("req", request)
    print("rom", request.POST.get('rooms'))
    print("post", request.POST.get('types'))
    print("post", request.POST.getlist('postal_codes'))

    print("get", request.GET)
    print("body", request.body)

    return render(request, 'house/index.html', context)


def get_house_by_id(request, id):
    return render(request, 'house/house.html', {
        'house': get_object_or_404(House, pk=id),
    })
