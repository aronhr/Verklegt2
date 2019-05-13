import sys
from django.http import JsonResponse
from django.contrib.humanize.templatetags.humanize import intcomma, date
from django.shortcuts import render, get_object_or_404
from house.models import *
from profiles.models import User


def true_or_false(name, request):
    true_false_list = [True, False]
    if name in request.GET:
        true_false_list = [True]

    return true_false_list


def index(request):
    p = HouseInfo.objects.all()
    if 'ajax' in request.GET:
        room_list = [x.rooms for x in HouseInfo.objects.all().distinct()]
        if 'rooms' in request.GET:
            room_list = request.GET.getlist('rooms')

        print(request)

        type_list = [x.id for x in HouseType.objects.all()]
        if 'types' in request.GET:
            type_list = request.GET.getlist('types')

        p_code_list = [x.id for x in PostalCodes.objects.all()]
        if 'p_code' in request.GET:
            p_code_list = request.GET.getlist('p_code')


        price_from = 0
        if 'price_from' in request.GET:
            price_from = request.GET.get('price_from')


        price_to = sys.maxsize
        if 'price_to' in request.GET:
            price_to = request.GET.get('price_to')

        size_from = 0
        if 'size_from' in request.GET:
            price_from = request.GET.get('size_from')

        size_to = sys.maxsize
        if 'size_to' in request.GET:
            size_to = request.GET.get('size_to')


        garage_list = true_or_false('garage', request)
        lift_list = true_or_false('elevator', request)
        extra_apart_list = true_or_false('extra_apartment', request)
        new_building_list = true_or_false('new_building', request)
        extra_entrance_list = true_or_false('entrance', request)



        db_houses = HouseInfo.objects.filter(

            rooms__in=room_list,
            house__p_code_id__in=p_code_list,
            garage__in=garage_list,
            type__in=type_list,
            elevator__in=lift_list,
            new_building__in=new_building_list,
            extra_apartment__in=extra_apart_list,
            entrance__in=extra_entrance_list,
            house__price__gte=price_from,
            house__price__lte=price_to,
            size__gte=size_from,
            size__lte=size_to
        )

        houses = []
        for x in db_houses:
            first_image = x.house.houseimage_set.first()
            image_src = "https://lh3.googleusercontent.com/uRXfIlcQBu-0hRfBHXcvWrDZjYu640sZL2JxQ3TJ4o1hAijbnXsS9zkJr9ZGjByp_Udei2XG=w640-h400-e365"
            if first_image is not None:
                image_src = first_image.image
            houses.append({
                'img_src': image_src,
                'address': f"{x.house.address} {x.house.street_nr}",
                'p_code': str(x.house.p_code),
                'price': intcomma(x.house.price),
                'desc': x.description,
                'type': x.type.type,
                'rooms': x.rooms,
                'size': x.size,
                'sellingdate': x.house.sellingdate,
                'garage': x.garage
            })

        return JsonResponse({'data': houses})
    context = {
        'houses': House.objects.filter(on_sale=True).order_by('id'),
        'house_info': HouseInfo.objects.all(),
        'types': HouseType.objects.all(),
        'towns': PostalCodes.objects.all(),
        'rooms': []
    }
    for i in context['house_info']:
        context['rooms'].append(i.rooms)

    context['rooms'] = sorted(set(context['rooms']))


    return render(request, 'house/index.html', context)


def get_house_by_id(request, id):
    house = get_object_or_404(House, pk=id)
    if request.user.is_active:
        history = History(user=request.user, house=house)
        history.save()
    return render(request, 'house/house.html', {
        'house': house,
    })
