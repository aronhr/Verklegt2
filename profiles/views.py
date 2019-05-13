from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from profiles.forms.profile_form import ProfileForm, UserForm, BankForm
from house.views import *
from profiles.forms.prop_form import *
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import user_passes_test
from profiles.models import UserBankInfo
from django.core import serializers

@login_required
def index(request):
    profile = Profile.objects.filter(user=request.user).first()
    user = User.objects.filter(id=profile.user.id).first()
    bank = UserBankInfo.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        userform = UserForm(instance=user, data=request.POST)
        bankfrom = BankForm(instance=bank, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            user = userform.save(commit=False)
            bank = bankfrom.save(commit=False)
            if len(request.FILES) != 0:
                myfile = request.FILES['myfile']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                profile.profile_pic = fs.url(filename)
            profile.user = request.user
            user.user = request.user
            bank.user = request.user
            profile.save()
            user.save()
            bank.save()
            return redirect('profile-index')
    return render(request, 'profile/index.html', {
        'form': ProfileForm(instance=profile),
        'userform': UserForm(instance=user),
        'bankform': BankForm(instance=bank),
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
            OnHold(house=house).save()
            return redirect('house-index')
    else:
        form = PropCreateForm()
        info = CreateHouseInfo()
    return render(request, 'profile/sell_property.html', {
        'houseForm': form,
        'houseInfo': info,
    })


@login_required
def wish_list(request):
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
    history = History.objects.filter(user=request.user)
    return render(request, 'profile/history.html', {
        'history': history
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
def my_props(request):
    props = House.objects.filter(seller=request.user)
    return render(request, 'profile/myProps.html', {
        'myProps': props
    })


@user_passes_test(lambda u: u.is_superuser)
def review_props_subs(request):
    onhold = OnHold.objects.all()
    return render(request, 'profile/reviewPropsSubmission.html', {
        'reviewPropsSubmissions': onhold
    })


@user_passes_test(lambda u: u.is_superuser)
def approve_submission(request, id):
    hold = get_object_or_404(OnHold, pk=id)
    house = get_object_or_404(House, pk=hold.house.id)
    house.on_sale = True
    house.save()
    return decline_submission(request, id)


@user_passes_test(lambda u: u.is_superuser)
def decline_submission(request, id):
    house = get_object_or_404(OnHold, pk=id)
    house.delete()
    return redirect('profile-review-properties-submissions')


@user_passes_test(lambda u: u.is_superuser)
def remove_user(request):
    return render(request, 'profile/delUser.html')


@user_passes_test(lambda u: u.is_superuser)
def remove_user_id(request, id):
    return render(request, 'profile/delUser.html', {
        'delUser': id
    })


@user_passes_test(lambda u: u.is_superuser)
def add_admin(request):
    return render(request, 'profile/addAdmin.html', {
        'addAdmin': 'This is where a add an admin'
    })


@user_passes_test(lambda u: u.is_superuser)
def remove_admin(request):
    return render(request, 'profile/removeAdmin.html', {
        'removeAdmin': 'This is where a remove an admin'
    })


@login_required
def edit_props(request):
    return render(request, 'profile/editProps.html', {
        'editProps': 'This is where i edit properties'
    })


@login_required
def del_property(request, id):
    house = get_object_or_404(House, pk=id)
    house.delete()
    return redirect('house-index')
