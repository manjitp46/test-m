# Generated by Django 2.0.3 on 2018-04-08 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listmovie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seatreserved',
            name='screening_id',
        ),
        migrations.RemoveField(
            model_name='seatreserved',
            name='seat_id',
        ),
        migrations.AddField(
            model_name='seatreserved',
            name='seat_id',
            field=models.ManyToManyField(to='listmovie.Seat'),
        ),
    ]