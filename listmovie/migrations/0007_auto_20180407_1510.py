# Generated by Django 2.0.3 on 2018-04-07 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listmovie', '0006_auto_20180407_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screening',
            name='screening_start',
            field=models.TimeField(),
        ),
    ]
