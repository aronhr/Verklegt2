from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from profiles.forms.profile_form import ProfileForm, UserForm
from house.views import *
from profiles.forms.prop_form import *
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import user_passes_test


@login_required
def index(request):
    profile = Profile.objects.filter(user=request.user).first()
    user = User.objects.filter(id=profile.user.id).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        userform = UserForm(instance=user, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            user = userform.save(commit=False)
            if len(request.FILES) != 0:
                myfile = request.FILES['myfile']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                profile.profile_pic = fs.url(filename)
            profile.user = request.user
            user.user = request.user
            profile.save()
            user.save()
            return redirect('profile-index')
    return render(request, 'profile/index.html', {
        'form': ProfileForm(instance=profile),
        'userform': UserForm(instance=user),
        'profile': profile
    })


@login_required
def sell_property(request):
    if request.method == 'POST':
        form = PropCreateForm(data=request.POST)
        info = CreateHouseInfo(data=request.POST)
        if form.is_valid() and info.is_valid():
            house = form.save(commit=False)
            house_info = info.save(commit=False)
            house.seller = request.user
            house.save()
            house_info.house = house
            house_info.save()
            fs = FileSystemStorage()
            for key in request.FILES.keys():
                for formfile in request.FILES.getlist(key):
                    house_image = HouseImage()
                    filename = fs.save(formfile.name, formfile)
                    house_image.image = fs.url(filename)
                    house_image.house = house
                    house_image.save()
            return redirect('profile-sell-property')
    else:
        form = PropCreateForm()
        info = CreateHouseInfo()
    return render(request, 'profile/sell_property.html', {
        'houseForm': form,
        'houseInfo': info,
    })


@login_required
def wishList(request):
    wish = WishList.objects.filter(user=request.user)
    return render(request, 'profile/wishList.html', {
        'wish': wish
    })


@login_required
def remove_wish(request, id):
    wish = get_object_or_404(WishList, pk=id)
    if wish.user == request.user:
        wish.delete()
    return redirect('profile-wishList')


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
    props = House.objects.filter(seller=request.user)
    return render(request, 'profile/myProps.html', {
        'myProps': props
    })


@user_passes_test(lambda u: u.is_superuser)
def reviewPropsSubs(request):
    return render(request, 'profile/reviewPropsSubmission.html', {
        'reviewPropsSubmissions': 'This is where a review properties submissions'
    })


@user_passes_test(lambda u: u.is_superuser)
def delUser(request):
    return render(request, 'profile/delUser.html', {
        'delUser': 'This is where i delete users'
    })


@user_passes_test(lambda u: u.is_superuser)
def addAdmin(request):
    return render(request, 'profile/addAdmin.html', {
        'addAdmin': 'This is where a add an admin'
    })


@user_passes_test(lambda u: u.is_superuser)
def removeAdmin(request):
    return render(request, 'profile/removeAdmin.html', {
        'removeAdmin': 'This is where a remove an admin'
    })


@login_required
def editProps(request):
    return render(request, 'profile/editProps.html', {
        'editProps': 'This is where i edit properties'
    })


@login_required
def delProperty(request, id):
    house = get_object_or_404(House, pk=id)
    house.delete()
    return redirect('house-index')
