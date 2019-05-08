from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    kt = models.CharField(max_length=10)
    dob = models.DateField()
    phone = models.CharField(max_length=9, blank=True)
    profile_pic = models.CharField(max_length=500)
    address = models.CharField(max_length=70)


class UserBankInfo(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    bank_nr = models.CharField(max_length=4)
    ledger = models.CharField(max_length=2)
    account_number = models.CharField(max_length=6)
