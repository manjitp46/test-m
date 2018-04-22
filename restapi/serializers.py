

from rest_framework import serializers
from listmovie.models import *
from rest_framework.fields import ReadOnlyField

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        
class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatre
        fields =  ("id",'movie_id', "name", "no_of_seats", "address", "seating_arrangement", "city_id")

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ('seat_no',)


class ReservationSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(source='user_id') 
#     movie_show = MovieShowSerializer(source="movie_show_id",)
    class Meta:
        model = Reservation
        fields = '__all__'


class BookedSeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('movie_show_id','seat_id')

        
#     def to_representation(self, instance):
#         ret = super(ReservationSerializer, self).to_representation(instance)
#         ret['username'] = ret['username'].lower()
#         return ret    
        

class MovieShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieShow
        fields =  '__all__'   
        
    
        