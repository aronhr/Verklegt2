# Generated by Django 2.2.1 on 2019-05-09 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.CharField(default='https://www.ibts.org/wp-content/uploads/2017/08/iStock-476085198.jpg', max_length=500),
        ),
    ]