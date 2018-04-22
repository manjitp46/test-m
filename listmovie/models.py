from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import default
from _datetime import datetime


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
    seating_category = models.ManyToManyField(SeatingCategory, default=None)
    
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
    
    class Meta:
        ordering = ['show_start']
        
#     seating_category = models.ManyToManyField(SeatingCategory)
    
    
    def __str__(self):
        return "{}".format(self.id)
#
#
class Seat(models.Model):
    seat_code = models.CharField(max_length=10, default='1_1')
    theatre_id = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{}".format(self.seat_code)
#
#
class ReservationType(models.Model):
    type = models.CharField(max_length=100)
    
    def __str__(self):
        return self.type
#
#
class Reservation(models.Model):
    no_of_seats_booked = models.IntegerField(default=0)
    movie_show_id = models.ForeignKey(MovieShow, on_delete=models.CASCADE)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=10)
    reservation_type_id = models.ForeignKey(ReservationType, on_delete=models.CASCADE)
    reservation_booking_date = models.DateField(default="2018-04-21")
    movie_show_date = models.DateField(default="2018-04-21")
    tranction_id = models.CharField(max_length=20)
    seat_id = models.ManyToManyField(Seat)
    amount = models.CharField(max_length=6, default=0)
    payment_status =  models.CharField(max_length=10, default="Pending")
    
    def __str__(self):
        return "{} {} {}".format(self.no_of_seats_booked, self.movie_show_id,  self.reservation_type_id)

class SeatReserved(models.Model):
    seat_id = models.ManyToManyField(Seat)
    reservation_id = models.ForeignKey(Reservation, on_delete=models.CASCADE)
#     screening_id = models.ForeignKey(MovieShow, on_delete=models.CASCADE)
