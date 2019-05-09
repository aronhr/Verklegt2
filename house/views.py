from django.http import JsonResponse
from django.contrib.humanize.templatetags.humanize import intcomma, date
from django.shortcuts import render, get_object_or_404
from house.models import *
from profiles.models import User


def index(request):
    p = HouseInfo.objects.all()
    if 'ajax' in request.GET:
        room_list = [x.rooms for x in HouseInfo.objects.all()]
        if 'rooms' in request.GET:
            room_list = request.GET.getlist('rooms')

        p_code_list = [x.id for x in PostalCodes.objects.all()]
        if 'p_code' in request.GET:
            p_code_list = request.GET.getlist('p_code')

        db_houses = HouseInfo.objects.filter(rooms__in=room_list, house__p_code_id__in=p_code_list)
        houses = [{
            'img_src': x.house.houseimage_set.first().image,
            'address': f"{x.house.address} {x.house.street_nr}",
            'p_code': str(x.house.p_code),
            'price': intcomma(x.house.price),
            'desc': x.description,
            'type': x.type.type,
            'rooms': x.rooms,
            'size': x.size,
            'sellingdate': x.house.sellingdate,

            # Þarf að fá upplýsingar um bæði houseInfo og house.. því ég leitae eftir mismundani upplýsingum.
            # for x in House.objects.filter(room=search_filter)
        } for x in db_houses]

        return JsonResponse({'data': houses})
    context = {
        'houses': House.objects.all(),
        'house_info': HouseInfo.objects.all(),
        'types': HouseType.objects.all(),
        'towns': PostalCodes.objects.all(),
        'rooms': []
    }
    for i in context['house_info']:
        context['rooms'].append(i.rooms)

    context['rooms'] = sorted(set(context['rooms']))

    print(str(p[0].id) in request.POST.getlist('postal_codes'))
    print("req", request)
    print("rom", request.POST.get('rooms'))
    print("post", request.POST.get('types'))
    print("post", request.POST.getlist('postal_codes'))

    return render(request, 'house/index.html', context)


def get_house_by_id(request, id):
    return render(request, 'house/house.html', {
        'house': get_object_or_404(House, pk=id),
    })
