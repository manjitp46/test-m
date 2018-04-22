# Generated by Django 2.0.3 on 2018-04-21 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listmovie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='amount',
            field=models.CharField(default=0, max_length=6),
        ),
        migrations.AddField(
            model_name='reservation',
            name='payment_status',
            field=models.CharField(default='Pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='movie_show_date',
            field=models.DateField(default='2018-04-21'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reservation_booking_date',
            field=models.DateField(default='2018-04-21'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='tranction_id',
            field=models.CharField(max_length=20),
        ),
    ]
