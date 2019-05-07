from django.shortcuts import render, get_object_or_404
from house.models import *

# Create your views here.


def index(request):
    return render(request, 'profile/index.html', {
        'profile': 'This is a profile'
    })


def sell_property(request):
    return render(request, 'profile/sell_property.html', {
        'sell_property': 'This is where you sell a property'
    })


def wishList(request):
    return render(request, 'profile/wishList.html', {
        'wishList': 'This is my wishList'
    })


def history(request):
    return render(request, 'profile/history.html', {
        'history': 'This is my search history'
    })


def offers(request):
    return render(request, 'profile/offers.html', {
        'offers': Offers.objects.all()
    })


def get_offer_by_id(request, id):
    return render(request, 'profile/offer_by_id.html', {
        'offer': get_object_or_404(Offers, pk=id)
    })


def myProps(request):
    return render(request, 'profile/myProps.html', {
        'myProps': 'This is my properties'
    })


def reviewPropsSubs(request):
    return render(request, 'profile/reviewPropsSubmission.html', {
        'reviewPropsSubmissions': 'This is where a review properties submissions'
    })


def delUser(request):
    return render(request, 'profile/delUser.html', {
        'delUser': 'This is where i delete users'
    })


def addAdmin(request):
    return render(request, 'profile/addAdmin.html', {
        'addAdmin': 'This is where a add an admin'
    })


def removeAdmin(request):
    return render(request, 'profile/removeAdmin.html', {
        'removeAdmin': 'This is where a remove an admin'
    })


def editProps(request):
    return render(request, 'profile/editProps.html', {
        'editProps': 'This is where i edit properties'
    })
