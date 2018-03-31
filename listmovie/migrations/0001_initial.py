# Generated by Django 2.0.3 on 2018-03-31 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=56)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=2000)),
                ('cast', models.TextField(max_length=500)),
                ('duration', models.FloatField()),
                ('poster', models.ImageField(max_length=500, upload_to='poster')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listmovie.Language')),
            ],
        ),
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('no_of_seats', models.IntegerField()),
                ('address', models.TextField(max_length=500)),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listmovie.City')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='theatres',
            field=models.ManyToManyField(to='listmovie.Theatre'),
        ),
    ]
