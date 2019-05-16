from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from profiles.forms.profile_form import ProfileForm, UserForm, BankForm
from house.views import *
from profiles.forms.prop_form import *
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import user_passes_test
from house.forms.buy_house_form import *
from profiles.forms.bank_form import *
from django.http import JsonResponse


@login_required
def index(request):
    offer = Offers.objects.filter(seller=request.user, seen=False)
    profile = Profile.objects.filter(user=request.user).first()
    user = User.objects.filter(id=profile.user.id).first()
    bank = UserBankInfo.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        userform = UserForm(instance=user, data=request.POST)
        bankfrom = BankForm(instance=bank, data=request.POST)
        if form.is_valid() and userform.is_valid() and bankfrom.is_valid():
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
    else:
        form = ProfileForm(instance=profile)
        userform = UserForm(instance=user)
        bankfrom = BankForm(instance=bank)
    return render(request, 'profile/index.html', {
        'form': form,
        'userform': userform,
        'bankform': bankfrom,
        'profile': profile,
        'offer': offer
    })


def profile_id(request, id):
    profile = get_object_or_404(User, pk=id)
    houses = House.objects.filter(seller=profile)
    return render(request, 'profile/profile.html', {
        'user': profile,
        'houses': houses
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
def toggle_wish_list(request, id):
    house = get_object_or_404(House, pk=id)
    if 'set' in request.GET:
        WishList(user=request.user, house=house).save()
    else:
        wish = get_object_or_404(WishList, house=id, user=request.user)
        if wish.user == request.user:
            wish.delete()
    return JsonResponse({'status': 'OK'}, status=200)


@login_required
def wish_list(request):
    wish = WishList.objects.filter(user=request.user)
    return render(request, 'profile/wishList.html', {
        'wish': wish
    })


@login_required
def remove_wish(request, id):
    wish = get_object_or_404(WishList, house=id, user=request.user)
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
def offers_seller(request):
    offers = Offers.objects.filter(seller=request.user, state=False)
    for x in offers:
        x.seen = True
        x.save()
    return render(request, 'profile/offers.html', {
        'seller': 'seller',
        'houses': offers
    })


@login_required
def offers_buyer(request):
    offers = Offers.objects.filter(user=request.user)
    return render(request, 'profile/offers.html', {
        'buyer': 'buyer',
        'houses': offers
    })


@login_required
def view_offer(request, id):
    my_offer = get_object_or_404(Offers, pk=id)
    if request.user != my_offer.seller:
        return redirect('profile-offers-seller')
    return render(request, 'profile/offer_by_id.html', {
        'my_offer': my_offer
    })


def mark_all_offers(id):
    offers = Offers.objects.filter(house=id)
    for x in offers:
        x.state = True
        x.save()


@login_required
def approve_offer(request, id):
    my_offer = get_object_or_404(Offers, pk=id)
    if request.user == my_offer.seller:
        house = get_object_or_404(House, pk=my_offer.house.id)
        house.on_sale = False
        house.save()
        my_offer.accepted = True
        my_offer.save()
        mark_all_offers(house.id)   # Offer skráð í 'deleted' state
        # Send email to buyer
    return redirect('profile-offers-seller')


@login_required
def decline_offer(request, id):
    my_offer = get_object_or_404(Offers, pk=id)
    if request.user == my_offer.seller:
        my_offer.state = True   # Offer skráð í 'deleted' state
        my_offer.save()
        # Send email to buyer
    return redirect('profile-offers-seller')


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
    users = User.objects.all()
    return render(request, 'profile/delUser.html', {'users': users})


@user_passes_test(lambda u: u.is_superuser)
def remove_user_id(request, id):
    user = get_object_or_404(User, pk=id)
    users = User.objects.all()
    if user == request.user:
        return render(request, 'profile/delUser.html',
                      {'error': 'Þú mátt ekki eyða þér sjálfum félagi!', 'users': users})
    user.delete()
    return redirect('profile-delete-user')


@user_passes_test(lambda u: u.is_superuser)
def add_admin(request):
    users = User.objects.filter(is_superuser=False)
    return render(request, 'profile/addAdmin.html', {
        'users': users
    })


@user_passes_test(lambda u: u.is_superuser)
def add_admin_id(request, id):
    user = get_object_or_404(User, pk=id)
    user.is_superuser = True
    user.save()
    return redirect('profile-add-admin')


@user_passes_test(lambda u: u.is_superuser)
def remove_admin(request):
    users = User.objects.filter(is_superuser=True)
    return render(request, 'profile/removeAdmin.html', {
        'users': users
    })


@user_passes_test(lambda u: u.is_superuser)
def remove_admin_id(request, id):
    user = get_object_or_404(User, pk=id)
    users = User.objects.all()
    if user == request.user:
        return render(request, 'profile/delUser.html',
                      {'error': 'Þú mátt ekki eyða þér sjálfum félagi!', 'users': users})
    user.is_superuser = False
    user.save()
    return redirect('profile-remove-admin')


@login_required
def edit_props(request, id):
    house = get_object_or_404(House, pk=id)
    house_info = get_object_or_404(HouseInfo, house=house.id)
    if house.seller == request.user or request.user.is_superuser:
        if request.method == 'POST':
            form = PropCreateForm(instance=house, data=request.POST)
            info = CreateHouseInfo(instance=house_info, data=request.POST)
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
            form = PropCreateForm(instance=house)
            info = CreateHouseInfo(instance=house_info)
        return render(request, 'profile/editProps.html', {
            'houseForm': form,
            'houseInfo': info,
        })


@login_required
def del_property(request, id):
    house = get_object_or_404(House, pk=id)
    if house.seller == request.user or request.user.is_superuser:
        house.delete()
    return redirect('house-index')


@login_required
def buy_property(request, id):
    house = get_object_or_404(House, pk=id)
    if request.method == 'POST':
        form = OfferForm(data=request.POST)
        card_info = CreateUserBankInfo(data=request.POST)
        if form.is_valid() and card_info.is_valid():
            Offers(price=request.POST['price'],
                   house=house,
                   user=request.user,
                   seller=house.seller
                   ).save()

            Card(user=request.user,
                 card_nr=request.POST['card_nr'],
                 exdate=request.POST['exdate'],
                 cvc=request.POST['cvc']
                 ).save()
        return render(request, 'profile/buy_property.html', {
            'submit_response': 'Tilboð þitt hefur verið sent',
            'house': house
        })
    else:
        form = OfferForm()
        card_info = CreateUserBankInfo()
    return render(request, 'profile/buy_property.html', {
        'offer_form': form,
        'bank_info': card_info,
        'house': house
    })
