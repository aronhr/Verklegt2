# Generated by Django 2.2.1 on 2019-05-06 21:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0002_offers_house'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='sellingdate',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]