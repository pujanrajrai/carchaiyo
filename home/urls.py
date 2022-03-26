from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('car/desc/<str:pk>', views.car_desc, name='car_desc'),
    path('search/', views.car_search, name='car_search'),
    path('watchlist/', views.watchlist, name='car_watchlist'),
    path('request/', views.request_visit, name='request_visit'),
    path('comment/', views.comment, name='comment'),
    path('mybookmark/', views.my_bookmark, name='my_bookmark'),
    path('myvisitreq/', views.my_visit_req, name='my_visit_req'),
    path('watchlist/remove/', views.remove_watchlist, name="remove_watchlist"),
    path('contactus/', views.contactus, name="contactus"),

]
