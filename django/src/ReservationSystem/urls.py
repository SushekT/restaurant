from django.urls import path
from . import views


app_name = 'ReservationSystem'


urlpatterns = [
    path('', views.reservetable, name='reservetable'),

]