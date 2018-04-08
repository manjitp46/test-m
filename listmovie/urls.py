from django.conf.urls import url
from .views import listmovie_home, list_theatre, select_show, list_seat
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^home$', listmovie_home),
    url(r'^theatre/(?P<movie_id>\d+)/(?P<city_id>\d+)/$', list_theatre, name="list_theatre"),
    url(r'^selectshow/(?P<movie_id>\d+)/(?P<theatre_id>\d+)/$', select_show, name="select_show"),
    url(r'^selectseat/(?P<movie_id>\d+)/(?P<theatre_id>\d+)$', list_seat, name="select_seat"),
    url(r'^login/$', auth_views.login, {'template_name': 'listmovie/login_user.html'})
]