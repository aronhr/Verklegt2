from django.db import models


class PostalCodes(models.Model):
    town = models.CharField(max_length=70)


# Create your models here.
class House(models.Model):
    address = models.CharField(max_length=255)
    street_nr = models.CharField(max_length=10, blank=True)
    price = models.SmallIntegerField()
    p_code = models.ForeignKey(PostalCodes, on_delete=models.SET_NULL)
    seller = models.ForeignKey('profiles.user', on_delete=models.CASCADE)
    on_sale = models.BooleanField(default=False)


class HouseType(models.Model):
    type = models.CharField(max_length=70)


class HouseInfo(models.Model):
    house_id = models.ForeignKey(House, on_delete=models.CASCADE)
    description = models.CharField(max_length=999)
    rooms = models.SmallIntegerField()
    size = models.CharField()
    type = models.ForeignKey(HouseType, on_delete=models.SET_NULL)
    garage = models.BooleanField(default=False)
    extra_apartment = models.BooleanField(default=False)
    new_building = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    entrance = models.BooleanField(default=False)


class HouseImages(models.Model):
    house_id = models.ForeignKey(House, on_delete=models.CASCADE)
    image = models.CharField(max_length=500)


class OnHold(models.Model):
    house_id = models.ForeignKey(House, on_delete=models.CASCADE)


class WishList(models.Model):
    user_id = models.ForeignKey('profiles.user', on_delete=models.CASCADE)
    house_id = models.ForeignKey(House, on_delete=models.CASCADE)


class History(models.Model):
    user_id = models.ForeignKey('profiles.user', on_delete=models.CASCADE)
    house_id = models.ForeignKey(House, on_delete=models.CASCADE)


class Offers(models.Model):
    user_id = models.ForeignKey('profiles.user', on_delete=models.CASCADE)
    seller_id = models.ForeignKey('profiles.user', on_delete=models.CASCADE)
    price = models.SmallIntegerField()
    date = models.DateTimeField(auto_now_add=True, blank=True)
    state = models.BooleanField(default=None)
