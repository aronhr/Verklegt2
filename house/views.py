from django.shortcuts import render, get_object_or_404, redirect
from house.models import *
from house.forms.prop_form import PropCreateForm


def index(request):
    p = PostalCodes.objects.all()
    context = {
        'houses': House.objects.all(),
        'types': HouseType.objects.all(),
        'towns': PostalCodes.objects.all(),
        'filter': {
            'postal_codes': request.POST.getlist('postal_codes'),
            'lyfta': request.POST.get('lyfta'),
            'rooms': request.POST.get('rooms')

        },
    }
    print(str(p[0].id) in request.POST.getlist('postal_codes'))
    print("req", request)
    print("post", request.POST.get('types'))
    print("post", request.POST.getlist('postal_codes'))

    print("get", request.GET)
    print("body", request.body)
    return render(request, 'house/index.html', context)


def get_house_by_id(request, id):
    return render(request, 'house/house.html', {
        'house': get_object_or_404(House, pk=id),
    })


def create_prop(request):
    if request.method == 'post':
        form = PropCreateForm(data=request.POST)
        if form.is_valid():
            house = form.save()
            house_image = HouseImage(image=request.POST['image'], house=house)
            house_image.save()
            return redirect('house-index')
    else:
        form = PropCreateForm()
    return render(request, 'house/create_prop.html', {
        'form': form
    })
