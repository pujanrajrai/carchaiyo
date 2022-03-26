from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from accounts.models import MyUser
from decorator import is_user, is_admin_or_user, is_admin
from cars.models import CarWatchlist, Comments, Car, CarBody,CarBrand


@is_admin_or_user()
def home(request):
    context = {
        'total_cars': Car.objects.all().count(),
        'total_comments': Comments.objects.all().count(),
        'total_car_body_type': CarBody.objects.all().count(),
        'total_users': MyUser.objects.all().count(),
        'total_book_marked': CarWatchlist.objects.all().count(),
        'total_car_brand': CarBrand.objects.all().count()
    }
    return render(request, 'dashboard/home.html', context)


@is_admin_or_user()
def property_visit_req(request):
    car_visit_list = CarWatchlist.objects.filter(car__user=request.user)
    context = {"car_visit_list": car_visit_list}
    return render(request, 'dashboard/car_visit_request.html', context)


@is_admin()
def all_user(request):
    context = {
        'users': MyUser.objects.all()

    }
    return render(request, 'dashboard/users_list.html', context)


@is_admin_or_user()
def my_cars(request):
    context = {
        'cars': Car.objects.filter(user=request.user)
    }
    return render(request, 'cars/car_list_view.html', context)


@is_admin_or_user()
def my_comment(request):
    context = {
        'comments': Comments.objects.filter(Q(car__user=request.user) | Q(user=request.user)).order_by(
            '-date_of_added')
    }
    return render(request, 'dashboard/my_comments.html', context)


@is_admin_or_user()
def remove_comment(request):
    if request.method == 'POST':
        try:
            Comments.objects.filter(Q(car__user=request.user) | Q(user=request.user)).filter(pk=request.POST['pk']).delete()
        except:
            pass

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
