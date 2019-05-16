from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    kt = models.CharField(max_length=10, blank=True)
    dob = models.DateField(blank=True)
    phone = models.CharField(max_length=9, blank=True)
    profile_pic = models.CharField(max_length=500, default='https://www.ibts.org/wp-content/uploads/2017/08/iStock-476085198.jpg', blank=True)
    address = models.CharField(max_length=70, blank=True)


class UserBankInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank_nr = models.CharField(max_length=4, blank=True)
    ledger = models.CharField(max_length=2, blank=True)
    account_number = models.CharField(max_length=6, blank=True)


class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_nr = models.CharField(max_length=20)
    exdate = models.CharField(max_length=5)     # mm/yy
    cvc = models.SmallIntegerField(max_length=3)
