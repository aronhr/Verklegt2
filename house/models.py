from django.db import models


class PostalCodes(models.Model):
    town = models.CharField(max_length=70)


# Create your models here.
class House(models.Model):
    address = models.CharField(max_length=255)
    street_nr = models.CharField(max_length=10, blank=True)
    price = models.SmallIntegerField()
    p_code = models.ForeignKey(PostalCodes, on_delete=models.CASCADE)
    seller = models.ForeignKey('profiles.user', on_delete=models.CASCADE)
    on_sale = models.BooleanField(default=False)


class HouseType(models.Model):
    type = models.CharField(max_length=70)


class HouseInfo(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    description = models.CharField(max_length=999)
    rooms = models.SmallIntegerField()
    size = models.CharField(max_length=200)
    type = models.ForeignKey(HouseType, on_delete=models.CASCADE)
    garage = models.BooleanField(default=False)
    extra_apartment = models.BooleanField(default=False)
    new_building = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    entrance = models.BooleanField(default=False)


class HouseImage(models.Model):
    image = models.CharField(max_length=500)
    house = models.ForeignKey(House, on_delete=models.CASCADE)

    def __str__(self):
        return self.image


class OnHold(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)


class WishList(models.Model):
    user = models.ForeignKey('profiles.user', on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)


class History(models.Model):
    user = models.ForeignKey('profiles.user', on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)


class Offers(models.Model):
    user = models.ForeignKey('profiles.user', on_delete=models.CASCADE, related_name="buyer")
    seller = models.ForeignKey('profiles.user', on_delete=models.CASCADE, related_name="seller")
    price = models.SmallIntegerField()
    date = models.DateTimeField(auto_now_add=True, blank=True)
    state = models.BooleanField(default=None)
