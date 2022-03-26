from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    # car body
    path('car_body/create/', views.CarBodyCreateView.as_view(), name='car_body_create'),
    path('car_body/list/', views.CarBodyListView.as_view(), name='car_body_list'),
    path('car_body/update/<str:pk>', views.CarBodyUpdateView.as_view(), name='car_body_update'),

    # car brand
    path('car_brand/create/', views.CarBrandCreateView.as_view(), name='car_brand_create'),
    path('car_brand/list/', views.CarBrandListView.as_view(), name='car_brand_list'),
    path('car_brand/update/<str:pk>', views.CarBrandUpdateView.as_view(), name='car_brand_update'),
    #
    # car
    path('car/create', views.CarCreateView.as_view(), name='car_create'),
    path('update/<str:pk>', views.CarUpdateView.as_view(), name='car_update_view'),
    path('list/', views.CarListView.as_view(), name='car_list_view'),

]
