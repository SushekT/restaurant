from django.urls import path
from . import views


app_name = 'aboutus'


urlpatterns = [
    path('', views.aboutus_list, name='AboutUs_list'),
]