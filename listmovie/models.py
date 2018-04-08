from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import default


# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=56, default=None)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class SeatingCategory(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    
    def __str__(self):
        return "{} {}".format(self.name, self.price)


# This Table is used to keep movie related info contains info in which city movie belongs to
class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    cast = models.TextField(max_length=500)
    duration = models.FloatField()
    poster = models.ImageField(upload_to="poster", max_length=500)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    city_id = models.ManyToManyField(City)

    def __str__(self):
        return "{0} ".format(self.name)



class Theatre(models.Model):
    name = models.CharField(max_length=256)
    no_of_seats = models.IntegerField()
    address = models.TextField(max_length=500)
    seating_arrangement = models.TextField(max_length=2000, null=True)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{0} {1}".format(self.name, self.city_id)




# class Auditorium(models.Model):
#     name = models.CharField(max_length=100)
#     no_of_seats = models.IntegerField()
#     theatre_id = models.ForeignKey(Theatre, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name
#
#
class Screening(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theatre_id = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    screening_start = models.TimeField()
    seating_category = models.ManyToManyField(SeatingCategory) 

class MovieShow(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theatre_id= models.ForeignKey(Theatre, on_delete=models.CASCADE)
    show_start= models.TimeField()
    show_end  = models.TimeField()  
    date = models.DateField()
#     seating_category = models.ManyToManyField(SeatingCategory)
    
    
    def __str__(self):
        return "{} {} {}".format(self.movie_id, self.theatre_id, self.show_start)
#
#
class Seat(models.Model):
    seat_no = models.IntegerField()
    theatre_id = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{} {}".format(self.seat_no, self.theatre_id)
#
#
class ReservationType(models.Model):
    type = models.CharField(max_length=100)
#
#
class Reservation(models.Model):
    movie_show_id = models.ForeignKey(MovieShow, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_type_id = models.ForeignKey(ReservationType, on_delete=models.CASCADE)

class SeatReserved(models.Model):
    seat_id = models.ForeignKey(Seat, on_delete=models.CASCADE)
    reservation_id = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    screening_id = models.ForeignKey(Screening, on_delete=models.CASCADE)
