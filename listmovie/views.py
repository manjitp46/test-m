from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
import uuid
from .utils import *
from django.http import JsonResponse
from .models import *
import json
import time
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
import datetime
from instamojo_wrapper import Instamojo
# Create your views here.
# sample Data preparing only For Bettiah So city Id is 1 and also refers as city


@csrf_exempt
def set_city_chosser(request):
    date = datetime.date.today()
    if request.POST:
        city_id = request.POST.get('city_id')
        request.session['city_id'] = city_id
        time.sleep(4)
        movies = Movie.objects.filter(city_id=city_id)
        return render(request, "listmovie/home.html", {'movies': movies, 'city_id': city_id, 'date':date})
    elif 'city_id' in request.session:
        city_id = request.session['city_id']
        movies = Movie.objects.filter(city_id=city_id)
#         return JsonResponse({'name':request.session['city_id']})
        return render(request, "listmovie/home.html", {'movies': movies, 'city_id': city_id, 'date':date})
    else:
        city_list = City.objects.all()
        return render(request, "listmovie/setup_city.html", {'city_list': city_list})     


def listmovie_home(request):
    request.session['member_id'] = '6464546465'
    movies = get_all_movies(city)
    return render(request, "listmovie/home.html", {'movies': movies, 'city_id': city})


# list_theatre takes two parameter and give all theatre wich is running in that city 

def list_theatre(request, movie_id, city_id, date=datetime.date.today()):
    movie_show = MovieShow.objects.all()
    movies =  Movie.objects.get(id=movie_id)
    now = datetime.datetime.now()
    current_day = now.day
    theatres = Theatre.objects.filter(movie_id=movie_id, city_id=city_id)
    theatre_show_time = dict()
    theatre_list = list(theatres)
    
    for t in theatre_list:
        theatre_show_time[t] = MovieShow.objects.filter(movie_id=movie_id, theatre_id=t.id,date=date)
    print(theatre_show_time)
#     show_timings = 
    return render(request, "listmovie/list_show.html",
                   {'theatres': theatres, 'movie_id':movie_id,
                    'current_day':current_day, 
                    'movie_name': movies.name,
                    'theatre_show_time':theatre_show_time})




def select_show(request, movie_id, theatre_id):
    theatre_with_screening = get_all_screening(movie_id, theatre_id)
    print(theatre_with_screening)
    return render(request, "listmovie/select_show.html", 
                  {'theatre_with_screening': theatre_with_screening, 'movie_id':movie_id, 'theatre_id':theatre_id})





def list_seat(request, movie_id, theatre_id,movie_show_id):
    theatre = Theatre.objects.get(id=theatre_id)
    # getting alreadybooked seat start here    
    reservation = Reservation.objects.filter(movie_show_id=movie_show_id).prefetch_related('seat_id')
    seat_booked_queryset = list()
    seat_booked_list = list()
    for seat in reservation:
        seat_booked_queryset.append(seat.seat_id.all())
    for seat_booked_query in seat_booked_queryset:
        for seat in seat_booked_query:
            seat_booked_list.append(seat.seat_code)
    print(seat_booked_list)
    # already booked seat end here      
    seats = theatre.seating_arrangement.split(",")
    seat_arrangement = [seat.replace("\n", '').replace("\r", '') for seat in seats]
    return render(request, "listmovie/show_seat.html",{'movie_id':movie_id, 
                        'theatre_id':theatre_id,
                        'movie_show_id':movie_show_id})

@csrf_exempt
def load_seat(request):
    input_data = json.loads(request.body.decode('utf-8'))
    theatre_id = input_data['theatre_id']
    movie_id = input_data['movie_id']
    movie_show_id = input_data['movie_show_id']            
    theatre = Theatre.objects.get(id=theatre_id)
    # getting alreadybooked seat start here    
    reservation = Reservation.objects.filter(movie_show_id=movie_show_id).prefetch_related('seat_id')
    seat_booked_queryset = list()
    seat_booked_list = list()
    for seat in reservation:
        seat_booked_queryset.append(seat.seat_id.all())
    for seat_booked_query in seat_booked_queryset:
        for seat in seat_booked_query:
            seat_booked_list.append(seat.seat_code)
    print(seat_booked_list)
    theatre = Theatre.objects.get(id=theatre_id)
    seating_arrangement = theatre.seating_arrangement.split(",")
    seat_arrangement = [seat.replace("\n", '').replace("\r", '') for seat in seating_arrangement]
    return JsonResponse({"booked_seat_list":seat_booked_list, 'seating_arrangement':seat_arrangement})
    

def handle_booking(request):
    if request.POST:
        total_input_price = request.POST.get('price');
        total_input_seats = request.POST.get('seats');
        movie_id = request.POST.get('movie_id')
        theatre_id = request.POST.get('theatre_id')
        movie_show_id = request.POST.get('movie_show_id')
        print(total_input_seats.split(","))
        
        movie = Movie.objects.get(id=movie_id)
        theatre = Theatre.objects.get(id=theatre_id)
        movie_show = MovieShow.objects.get(id=movie_show_id)
        return render(request, 'listmovie/booking_detail.html', 
        {"price":total_input_price, 'seats':total_input_seats.split(","),
         'movie':movie, "theatre":theatre, 'movie_show':movie_show
         })
    else:
        return render(request, 'listmovie/booking_detail.html')
    
def handle_user_details(request):
    if request.POST:
        total_input_price = request.POST.get('price');
        total_input_seats = request.POST.get('seats');
        movie_id = request.POST.get('movie_id')
        theatre_id = request.POST.get('theatre_id')
        movie_show_id = request.POST.get('movie_show_id')
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        movie = Movie.objects.get(id=movie_id)
        reservation_type = ReservationType.objects.get(id=1)
        theatre = Theatre.objects.get(id=theatre_id)
        movie_show = MovieShow.objects.get(id=movie_show_id)
        total_input_seats_arr = total_input_seats.split(",");
        seats_arr = [Seat.objects.get(seat_code=seat, theatre_id=theatre_id) for seat in total_input_seats_arr]
        print(seats_arr)
        response = make_payments(amount=total_input_price,email=email,mobile=mobile)
        if(response['success']):
            reservation = Reservation(no_of_seats_booked=len(seats_arr),movie_show_id=movie_show,
                                      reservation_type_id=reservation_type,reservation_booking_date=datetime.date.today(),
                                      movie_show_date=movie_show.date, email=email, amount = total_input_price,
                                      mobile_no=mobile, tranction_id=response['payment_request']['id'])
            
            reservation.save()
            reservation.seat_id.set(seats_arr)
            return redirect(response['payment_request']['longurl'])
#             return render(request, 'listmovie/user_details.html')
    else:
        return render(request, 'listmovie/user_details.html')
    

def make_payments(amount, email, mobile, name="Manjit"):
    
    api = Instamojo(api_key="test_d937681fc5e6122829fc0dbd454",
                    auth_token="test_a64dbd2399c9ef2b08277eb8c86",endpoint='https://test.instamojo.com/api/1.1/')
    
    # Create a new Payment Request
    response = api.payment_request_create(
        amount=amount,
        purpose='Movie Booking',
        send_email=True,
        email=email,
        buyer_name= name,
        phone = mobile,
        allow_repeated_payments=False,
        redirect_url="http://localhost:8000/listmovie/user_details"
        )
    # print the long URL of the payment request.
    print(response)
    return response

def get_payment_status(payment_request_id, payment_id):
    api = Instamojo(api_key="test_d937681fc5e6122829fc0dbd454",
                    auth_token="test_a64dbd2399c9ef2b08277eb8c86",endpoint='https://test.instamojo.com/api/1.1/')
    
    response = api.payment_request_payment_status(payment_request_id, payment_id)
    print(response)
    return response


@csrf_exempt
def verify_payment(request):
    input_data = json.loads(request.body.decode('utf-8'))
    payment_id = input_data['payment_id']
    payment_request_id = input_data['payment_request_id']
    response = get_payment_status(payment_request_id=payment_request_id, payment_id=payment_id)
    reservation = Reservation.objects.get(tranction_id=payment_request_id)
    reservation.payment_status = response['payment_request']['status']
    reservation.save()
    return JsonResponse(response)
    
# def handle_checkbooking(request, movie_id, theatre_id, screening_id):
        
