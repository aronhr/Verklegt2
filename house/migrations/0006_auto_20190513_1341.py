# Generated by Django 2.2.1 on 2019-05-13 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0005_auto_20190512_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='state',
            field=models.BooleanField(default=False),
        ),
    ]