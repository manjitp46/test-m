from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from .views import *

router = routers.DefaultRouter()
router.register(r'city', CityViewSet)
router.register(r'movie', MovieViewSet)
router.register(r'movie/(?P<city_id>\d+)', MovieViewSet)
router.register(r'theatre', TheatreViewSet)
router.register(r'reservation', ReservationViewSet)
router.register(r'reservation/(?P<movie_show_id>\d+)/(?P<movie_show_date>[\w\-\.]+)/', ReservationViewSet)
router.register(r'theatre/(?P<movie_id>\d+)/(?P<city_id>\d+)', TheatreViewSet)
router.register(r'movieshow', MovieShowViewSet)
router.register(r'movieshow/(?P<movie_id>\d+)/(?P<theatre_id>\d+)/(?P<date>[\w\-\.]+)/', MovieShowViewSet)
schema_view = get_swagger_view(title='Swagger API')
urlpatterns = [
       url(r'^docs/', schema_view),
]

urlpatterns += router.urls