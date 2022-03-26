from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # # property category
    path('', views.home, name='home'),
    path('visit/req/', views.property_visit_req, name='property_visit_req'),
    path('all/users/', views.all_user, name='all_users'),
    path('my/properties/', views.my_cars, name='my_cars'),
    path('my/comments/', views.my_comment, name='my_comments'),
    path('delete/comments/', views.remove_comment, name='remove_comment')
]
