from django.db import models

# Create your models here.


class User(models.Model):
    kt = models.CharField(max_length=10)
    dob = models.DateField()
    email = models.CharField(max_length=55)
    name = models.CharField(max_length=70)
    user_name = models.CharField(max_length=55)
    profile_pic = models.CharField(max_length=500)
    password = models.CharField(max_length=55)
    adddress = models.CharField(max_length=70)


class UserBankInfo(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    bank_nr = models.CharField(max_length=4)
    ledger = models.CharField(max_length=2)
    account_number = models.CharField(max_length=6)


class Admin(models.Model):
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE)



