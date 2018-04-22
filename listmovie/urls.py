from django.conf.urls import url
from .views import listmovie_home, list_theatre, select_show, list_seat,set_city_chosser,load_seat, handle_booking, handle_user_details, verify_payment
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^index$', set_city_chosser, name="index"),
    url(r'^home$', listmovie_home),
    url(r'^theatre/(?P<movie_id>\d+)/(?P<city_id>\d+)/(?P<date>[\w\-\.]+)/$', list_theatre, name="list_theatre"),
    url(r'^selectshow/(?P<movie_id>\d+)/(?P<theatre_id>\d+)/$', select_show, name="select_show"),
    url(r'^selectseat/(?P<movie_id>\d+)/(?P<theatre_id>\d+)/(?P<movie_show_id>\d+)$', list_seat, name="select_seat"),
    url(r'^login/$', auth_views.login, {'template_name': 'listmovie/login_user.html'}),
    url(r'^api/load_seat$', load_seat, name='load_seat'),
    url(r'^api/update_status$', verify_payment, name='update_status'),
    url(r'^handle_booking$', handle_booking, name='handle_booking'),
    url(r'^user_details$', handle_user_details, name='handle_user_details')
]