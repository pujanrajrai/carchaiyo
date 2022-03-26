from django.contrib import admin
from .models import CarBody,CarBrand,Car,Comments,CarWatchlist,FuelType,Transmission
# Register your models here.
admin.site.register(Car)
admin.site.register(CarBody)
admin.site.register(CarBrand)
admin.site.register(CarWatchlist)
admin.site.register(Comments)
admin.site.register(FuelType)
admin.site.register(Transmission)