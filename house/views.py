from django.shortcuts import render, get_object_or_404
from house.models import *
from profiles.models import User


def index(request):
    context = {'houses': House.objects.all()}
    return render(request, 'house/index.html', context)


def get_house_by_id(request, id):
    return render(request, 'house/house.html', {
        'house': get_object_or_404(House, pk=id),
    })
