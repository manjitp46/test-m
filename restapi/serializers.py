

from rest_framework import serializers
from listmovie.models import *
from django.contrib.contenttypes import fields

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        
class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatre
        fields =  ("id",'movie_id', "name", "no_of_seats", "address", "seating_arrangement", "city_id")

class MovieShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieShow
        fields =  '__all__'        