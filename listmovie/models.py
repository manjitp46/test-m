from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=56, default=None)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Theatre(models.Model):
    name = models.CharField(max_length=256)
    no_of_seats = models.IntegerField()
    address = models.TextField(max_length=500)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} {1}".format(self.name, self.city_id)


# This Table is used to keep movie related info contains info in which city movie belongs to
class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    cast = models.TextField(max_length=500)
    duration = models.FloatField()
    poster = models.ImageField(upload_to="poster", max_length=500)
    theatres = models.ManyToManyField(Theatre)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def list_display_movie(self):
        return "\n".join([t.__str__() for t in self.theatres.all()])

    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6}".format(self.name, self.description, self.cast, self.duration, self.theatres, self.poster
                                            , self.language)


# class Auditorium(models.Model):
#     name = models.CharField(max_length=100)
#     no_of_seats = models.IntegerField()
#     theatre_id = models.ForeignKey(Theatre, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name
#
#
# class Screening(models.Model):
#     movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     auditorium_id = models.ForeignKey(Auditorium, models.CASCADE)
#     screening_start = models.DateTimeField()
#
#
# class Seat(models.Model):
#     row = models.IntegerField()
#     col = models.IntegerField()
#     auditorium_id = models.ForeignKey(Auditorium, on_delete=models.CASCADE)
#
#
# class ReservationType(models.Model):
#     type = models.CharField(max_length=100)
#
#
# class Reservation(models.Model):
#     screening_id = models.ForeignKey(Screening, on_delete=models.CASCADE)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     reservation_type_id = models.ForeignKey(ReservationType, on_delete=models.CASCADE)
#
#
#
#
# class SeatReserved(models.Model):
#     seat_id = models.ForeignKey(Seat, on_delete=models.CASCADE)
#     reservation_id = models.ForeignKey(Reservation, on_delete=models.CASCADE)
#     screening_id = models.ForeignKey(Screening, on_delete=models.CASCADE)
