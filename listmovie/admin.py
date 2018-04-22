from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "cast","poster", "language")
    # list_editable = ("name", "description", "cast", "city_id")


@admin.register(Reservation)
class Reservation(admin.ModelAdmin):
    list_display = ('id', 'no_of_seats_booked', 'movie_show_id',
                     'email', 'reservation_type_id',
                      'reservation_booking_date', 'movie_show_date',
                      'movie_show_date', 'tranction_id', 'amount', 'payment_status')


@admin.register(Seat)
class CityAdmin(admin.ModelAdmin):
    list_display = ("id", "seat_code", 'theatre_id')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Theatre)
class TheatreAdmin(admin.ModelAdmin):
    list_display = ("name", "city_id")


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(MovieShow)
admin.site.register(Screening)
admin.site.register(SeatingCategory)
admin.site.register(ReservationType)
# admin.site.register(Reservation)
admin.site.register(SeatReserved)
