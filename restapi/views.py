from django.shortcuts import render
from datetime import date
# Create your views here.
import sys
from locale import currency
sys.path.append("../")
from rest_framework import viewsets
from listmovie.models import *
from .serializers import *
from rest_framework.permissions import BasePermission

# Authentication
SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']

class IsAuthenticatedOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        if (request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated()):
            return True
        return False


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
class TheatreViewSet(viewsets.ModelViewSet):
    queryset = Theatre.objects.all()
    serializer_class = TheatreSerializer   
    
    def get_queryset(self):
        """
        This view should return a list of all the Movie
        For A city.
        """
        movie_id = self.kwargs.get('movie_id')
        city_id = self.kwargs.get('city_id')
        if city_id is not None and movie_id is not None:
            return Theatre.objects.filter(city_id=city_id, movie_id=movie_id)  
        else:
            return Theatre.objects.all()
        
class MovieShowViewSet(viewsets.ModelViewSet):
    queryset = MovieShow.objects.all()
    serializer_class = MovieShowSerializer   
    
    def get_queryset(self):
        """
        This view should return a list of all the Movie
        Show for a movie.
        """
        theatre_id = self.kwargs.get('theatre_id')
        movie_id = self.kwargs.get('movie_id')
        input_date = self.kwargs.get('date')
        print(input_date,theatre_id,movie_id)
        
        if theatre_id is not None and movie_id is not None and input_date is not None:
            day, month, year = map(int, input_date.split("-"))
            current_date = date(year, month, day)
            print("inside if")
            return MovieShow.objects.filter(movie_id=movie_id, theatre_id=theatre_id, date=current_date)
            
        else:
            return MovieShow.objects.all()
        
        
       