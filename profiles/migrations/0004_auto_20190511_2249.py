# Generated by Django 2.2.1 on 2019-05-11 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20190509_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbankinfo',
            name='account_number',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='userbankinfo',
            name='bank_nr',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AlterField(
            model_name='userbankinfo',
            name='ledger',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]
