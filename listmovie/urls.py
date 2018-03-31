from django.conf.urls import url
from .views import listmovie_home, list_theatre

urlpatterns = [
    url(r'^home$', listmovie_home),
    url(r'^theatre/(?P<movie_id>\d+)/(?P<city_id>\d+)/$', list_theatre, name="list_theatre")
]