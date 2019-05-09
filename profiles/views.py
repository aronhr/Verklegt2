from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from profiles.forms.profile_form import ProfileForm, UserForm
from house.views import *
from profiles.forms.prop_form import *
from django.core.files.storage import FileSystemStorage


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
# TODO: Fix why this thing is not posting to the data base, also make code sexy
def sell_property(request):
    all_h_types = [x for x in HouseType.objects.all()]
    if request.method == 'POST':
        form = PropCreateForm(data=request.POST)
        info = CreateHouseInfo(data=request.POST)
        h_type = CreateHouseType(data=request.POST)
        if form.is_valid() and info.is_valid() and h_type.is_valid():
            house = form.save(commit=False)
            house_info = info.save(commit=False)
            house_type = h_type.save(commit=False)
            house.seller = request.user
            house.on_sale = False
            house_info.house = house.id
            house_info.type = house_type.type
            house_image = HouseImage(image=request.POST['image'], house=house)
            house.save()
            house_info.save()
            house_image.save()
            house_type.save()
            return redirect('house-index')
    else:
        form = PropCreateForm()
        info = CreateHouseInfo()
        h_type = CreateHouseType()
    return render(request, 'house/create_prop.html', {
        'houseForm': form,
        'houseInfo': info,
        'houseType': h_type,
        'all_h_type': all_h_types
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
