from django.shortcuts import render
from .utils import *

# Create your views here.
# sample Data preparing only For Bettiah So city Id is 1 and also refers as city

city = 1


def listmovie_home(request):
    theatres = get_all_theatre(city)
    movies = [get_all_movies(t) for t in theatres]
    return render(request, "listmovie/home.html", {'movies': movies, 'city_id': city})


def list_theatre(request, movie_id, city_id):
    movies = Movie.objects.get(id=movie_id)
    theatres = movies.theatres.filter(city_id=city_id)
    return render(request, "listmovie/list_theatre.html", {'theatres': theatres})
