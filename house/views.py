from django.shortcuts import render, get_object_or_404


# Create your views here.
def index(request):
    return render(request, 'house/index.html', {
        'houses': 'this is all houses'
    })


def get_house_by_id(request, id):
    return render(request, 'house/house.html', {
        'house': 'this is house with id: ' + str(id)
    })
