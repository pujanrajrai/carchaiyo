from django.contrib import messages
from django.db.models import F, Q
from django.shortcuts import render

from cars.models import Car, CarBody, CarBrand, CarWatchlist, Comments, Transmission
from django.http import Http404, HttpResponseRedirect

from .forms import ContactForm
from decorator import is_user, is_admin_or_user, is_admin


# Create your views here.
def home(request):
    car = Car.objects.filter(is_available=True).filter(is_blocked=False).filter(is_available=True)
    context = {
        'cars': car.order_by('-total_click')[:6],
        'brands': CarBrand.objects.all(),
        'bodies': CarBody.objects.all(),
        'tranmissions': Transmission.objects.all(),
        'wagon_count': car.filter(body_type__body_type='Wagon').count(),
        'pickup_count': car.filter(body_type__body_type='Pickup').count(),
        'mini_van_count': car.filter(body_type__body_type='Minivan/Van').count(),
        'crossover_count': car.filter(body_type__body_type='Crossover').count(),
        'suv_count': car.filter(body_type__body_type='SUV').count(),
        'hatchback_count': car.filter(body_type__body_type='Hatchback').count(),
        'coupe_count': car.filter(body_type__body_type='Coupe').count(),
        'sedan_count': car.filter(body_type__body_type='Sedan').count(),
    }
    # to differentiate between watchlist and non watchlist proties
    try:
        watchlist = CarWatchlist.objects.filter(user=request.user)
        watchlist_properties = []
        for watch in watchlist:
            watchlist_properties.append(watch.car)
        context['watchlist_properties'] = watchlist_properties
    except:
        pass


    return render(request, 'home/home.html', context)



def car_desc(request, pk):
    try:
        car = Car.objects.get(pk=pk)
        Car.objects.filter(pk=pk).update(total_click=F('total_click') + 1)

        comments = Comments.objects.filter(car__pk=pk).order_by('-date_of_added')
    except Car.DoesNotExist:
        raise Http404
    context = {
        'car': car,
        'comments': comments
    }

    try:
        is_requested = CarWatchlist.objects.filter(user=request.user).filter(car__pk=pk).filter(
            is_cart_visit=True).exists()
        context['is_requested'] = is_requested

    except:
        pass
    return render(request, 'home/car_desc.html', context)


# # for searching properties
def car_search(request):
    car = Car.objects.filter(is_available=True).filter(is_blocked=False).filter(is_available=True)
    context = {
        'brands': CarBrand.objects.all(),
        'bodies': CarBody.objects.all(),
        'tranmissions': Transmission.objects.all(),
    }

    if request.method == 'GET':
        if request.GET['brands']:
            brands = request.GET['brands']
        else:
            brands = 'any'

        if request.GET['bodies']:
            bodies = request.GET['bodies']
        else:
            bodies = 'bodies'

        if request.GET['tranmissions']:
            tranmissions = request.GET['tranmissions']
        else:
            tranmissions = 'any'

        # user search properties logic
        try:
            if request.GET['price']:
                price = int(request.GET['price'])
                context['price'] = price
                if price == 100000:
                    car = car.filter(price__lte=100000)
                elif price == 1000000:

                    car = car.filter(price__gt=100000).filter(price__lte=1000000)
                elif price == 5000000:
                    car = car.filter(price__gt=1000000).filter(price__lte=5000000)
                elif price == 10000000:
                    car = car.filter(price__gt=5000000).filter(price__lte=10000000)
                elif price == 10000001:
                    car = car.filter(price__gt=10000000)
                else:
                    car = car.filter(price__lt=0)

        except:
            pass
        # searching through different criteria
        if brands != 'any':
            car = car.filter(brand__brand=brands)
        if bodies != 'any':
            car = car.filter(body_type__body_type=bodies)
        if tranmissions != 'any':
            car = car.filter(transmission__transmission=tranmissions)
        if car.count() == 0:
            context['no_data'] = 'The Car is not available in this search Criteria'
        context['cars'] = car
        context['car_body'] = bodies
        context['car_brand'] = brands
        context['car_tranmissions'] = tranmissions

        try:
            watchlist = CarWatchlist.objects.filter(user=request.user)
            watchlist_properties = []
            for watch in watchlist:
                watchlist_properties.append(watch.car)
            context['watchlist_properties'] = watchlist_properties
        except:
            pass

    return render(request, 'home/car_search.html', context)

@is_admin_or_user()
def watchlist(request):
    if request.method == 'POST':
        try:
            CarWatchlist.objects.create(
                user=request.user,
                car=Car.objects.get(pk=request.POST['car_id'])
            )
        except :
            pass
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@is_admin_or_user()
def request_visit(request):
    if request.method == 'POST':
        # try:
            car_watchlist = CarWatchlist.objects.filter(user=request.user).filter(
                car__pk=request.POST['car_id'])
            if car_watchlist.exists():
                car_watchlist.update(is_cart_visit=True)
            else:
                CarWatchlist.objects.create(
                    user=request.user,
                    car=Car.objects.get(pk=request.POST['car_id']),
                    is_cart_visit=True
                )
        # except:
        #     print("error")
        #     pass

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@is_admin_or_user()
def comment(request):
    if request.method == 'POST':
        try:
            Comments.objects.create(
                user=request.user,
                car=Car.objects.get(pk=request.POST['car_id']),
                comment=request.POST['comment']
            )
            messages.success(request, 'Comment Added Successfully', extra_tags={'comment_success_message'})
        except:
            messages.success(request, 'something went wrong', extra_tags={'comment_error_message'})

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@is_admin_or_user()
def my_bookmark(request):
    context = {'bookmarks': CarWatchlist.objects.filter(user=request.user).filter(is_cart_visit=False)}
    return render(request, 'home/bookmark.html', context)


@is_admin_or_user()
def my_visit_req(request):
    context = {'bookmarks': CarWatchlist.objects.filter(user=request.user).filter(is_cart_visit=True)}
    return render(request, 'home/car_visit_req.html', context)


@is_admin_or_user()
def remove_watchlist(request):
    try:
        CarWatchlist.objects.filter(Q(car__user=request.user) | Q(user=request.user)).filter(
            car=Car.objects.get(pk=request.POST['car_id'])).delete()
    except:
        pass
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def contactus(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            context['message'] = 'Contact form submitted successfully'
        else:
            context['message'] = form.errors
    return render(request, 'home/contactus.html', context)
