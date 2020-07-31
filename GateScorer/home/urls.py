from django.urls import path
from . import views


app_name='home'
urlpatterns=[
    path('', views.index , name='index'),
    path( 'h_index/' , views.home_index, name='hindex'),
    path( 'about/',views.about,name='about'),
]