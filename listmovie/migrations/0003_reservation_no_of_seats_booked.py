# Generated by Django 2.0.3 on 2018-04-08 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listmovie', '0002_auto_20180408_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='no_of_seats_booked',
            field=models.IntegerField(default=0),
        ),
    ]
