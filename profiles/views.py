from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from house.models import *
from profiles.models import Profile
#from profiles.forms.profile_form import ProfileForm
from django.contrib.auth.models import User


@login_required
def index(request):
    """profile = Profile.objects.filter(user=request.user).first()
    user = User.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile-index')
    return render(request, 'profile/index.html', {
        'form': ProfileForm(instance={profile, user})
    })
"""
    pass

@login_required
def sell_property(request):
    return render(request, 'profile/sell_property.html', {
        'sell_property': 'This is where you sell a property'
    })


@login_required
def wishList(request):
    return render(request, 'profile/wishList.html', {
        'wishList': 'This is my wishList'
    })


@login_required
def history(request):
    return render(request, 'profile/history.html', {
        'history': 'This is my search history'
    })


@login_required
def offers(request):
    return render(request, 'profile/offers.html', {
        'offers': Offers.objects.all()
    })


@login_required
def get_offer_by_id(request, id):
    return render(request, 'profile/offer_by_id.html', {
        'offer': get_object_or_404(Offers, pk=id)
    })


@login_required
def myProps(request):
    return render(request, 'profile/myProps.html', {
        'myProps': 'This is my properties'
    })


@login_required
def reviewPropsSubs(request):
    return render(request, 'profile/reviewPropsSubmission.html', {
        'reviewPropsSubmissions': 'This is where a review properties submissions'
    })


@login_required
def delUser(request):
    return render(request, 'profile/delUser.html', {
        'delUser': 'This is where i delete users'
    })


@login_required
def addAdmin(request):
    return render(request, 'profile/addAdmin.html', {
        'addAdmin': 'This is where a add an admin'
    })


@login_required
def removeAdmin(request):
    return render(request, 'profile/removeAdmin.html', {
        'removeAdmin': 'This is where a remove an admin'
    })


@login_required
def editProps(request):
    return render(request, 'profile/editProps.html', {
        'editProps': 'This is where i edit properties'
    })
