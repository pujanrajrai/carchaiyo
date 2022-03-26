from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.utils.decorators import method_decorator

from .forms import CarForm, CarBodyForm, CarBrandForm
from django.views.generic import CreateView, ListView, UpdateView
from .models import CarBody, CarBrand, Transmission, FuelType, Car
from decorator import is_user, is_admin_or_user, is_admin


# Create your views here.

@method_decorator(is_admin(), name='dispatch')
class CarBodyCreateView(SuccessMessageMixin, CreateView):
    form_class = CarBodyForm
    template_name = 'cars/car_body_create_update.html'
    success_url = '/cars/car_body/list/'
    success_message = 'Car body Successfully Create'


@method_decorator(is_admin(), name='dispatch')
class CarBodyListView(ListView):
    model = CarBody
    context_object_name = 'car_body'
    template_name = 'cars/car_body_list_view.html'


@method_decorator(is_admin(), name='dispatch')
class CarBodyUpdateView(SuccessMessageMixin, UpdateView):
    form_class = CarBodyForm
    model = CarBody
    template_name = 'cars/car_body_create_update.html'
    success_url = '/cars/car_body/list/'
    success_message = 'Car body Successfully Updated'


# car brand start

@method_decorator(is_admin(), name='dispatch')
class CarBrandCreateView(SuccessMessageMixin, CreateView):
    form_class = CarBrandForm
    template_name = 'cars/car_brand_create_update.html'
    success_url = '/cars/car_brand/list/'
    success_message = 'Car Brand Successfully Create'


@method_decorator(is_admin(), name='dispatch')
class CarBrandListView(ListView):
    model = CarBrand
    context_object_name = 'car_brand'
    template_name = 'cars/car_brand_list_view.html'


@method_decorator(is_admin(), name='dispatch')
class CarBrandUpdateView(SuccessMessageMixin, UpdateView):
    form_class = CarBrandForm
    model = CarBrand
    template_name = 'cars/car_brand_create_update.html'
    success_url = '/cars/car_brand/list/'
    success_message = 'Car body Successfully Updated'


@method_decorator(is_admin_or_user(), name='dispatch')
class CarCreateView(SuccessMessageMixin, CreateView):
    form_class = CarForm
    template_name = 'cars/car_create_update.html'
    success_message = 'Car Created Successfully'
    success_url = '/dashboard/my/properties/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


@method_decorator(is_admin(), name='dispatch')
class CarListView(ListView):
    model = Car
    context_object_name = 'cars'
    template_name = 'cars/car_list_view.html'


@method_decorator(is_admin_or_user(), name='dispatch')
class CarUpdateView(SuccessMessageMixin, UpdateView):
    form_class = CarForm
    model = Car
    template_name = 'cars/car_create_update.html'
    success_message = 'Car Created Successfully'
    success_url = '/dashboard/my/properties/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

