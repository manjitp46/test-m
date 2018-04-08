from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .utils import *
import pdb
from builtins import str
from django.contrib.auth import views as auth_views

# Create your views here.
# sample Data preparing only For Bettiah So city Id is 1 and also refers as city

city = 1


def listmovie_home(request):
    movies = get_all_movies(city)
    return render(request, "listmovie/home.html", {'movies': movies, 'city_id': city})


# list_theatre takes two parameter and give all theatre wich is running in that city 

def list_theatre(request, movie_id, city_id):
    theatres = get_all_theatre(movie_id, city_id)
    return render(request, "listmovie/list_theatre.html",
                   {'theatres': theatres, 'movie_id':movie_id})

def select_show(request, movie_id, theatre_id):
    theatre_with_screening = get_all_screening(movie_id, theatre_id)
    print(theatre_with_screening)
    return render(request, "listmovie/select_show.html", 
                  {'theatre_with_screening': theatre_with_screening, 'movie_id':movie_id, 'theatre_id':theatre_id})

def list_seat(request, movie_id, theatre_id):
    theatre = Theatre.objects.get(id=theatre_id)
    seats = theatre.seating_arrangement.split(",")
    seat_arrangement = [seat.replace("\n", '').replace("\r", '') for seat in seats]
    print(request.user)
    return render(request, "listmovie/show_seat.html",
                   {'seat_arrangement': ",".join(seat_arrangement)})


# def handle_checkbooking(request, movie_id, theatre_id, screening_id):
        
