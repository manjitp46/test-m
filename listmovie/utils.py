from .models import *


def get_all_theatre(city_id):
    theatre = Theatre.objects.filter(city_id__id=city_id)
    return theatre


def get_all_movies(theatre):
    movies = Movie.objects.filter(theatres=theatre)
    return movies
