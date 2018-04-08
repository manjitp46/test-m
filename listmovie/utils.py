from .models import *


def get_all_theatre(movie_id, city_id):
    theatre = Theatre.objects.filter(movie_id=movie_id, city_id=city_id)
    return theatre


def get_all_movies(city_id):
    movies = Movie.objects.filter(city_id=city_id)
    return movies

def get_all_screening(movie_id, theatre_id):
    theatre_with_screening = Screening.objects.filter(theatre_id=theatre_id, movie_id=movie_id)
    return theatre_with_screening


# def check_if_movie_is_already_in_set(movies_list, movie):
#     if len(movies_list) is 0:
#         return False
#     else:
#         for m in movies_list:
#             for list_item, movie_item in m, movie:
#                 if list_item.id == movie_item.id:
#                     return True
#                 else:
#                     return False 
#         return False

