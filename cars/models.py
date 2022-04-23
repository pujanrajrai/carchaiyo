from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from accounts.models import MyUser


class CarBody(models.Model):
    body_type = models.CharField(max_length=50)

    def __str__(self):
        return self.body_type


class CarBrand(models.Model):
    brand = models.CharField(max_length=50)

    def __str__(self):
        return self.brand


class FuelType(models.Model):
    fuel = models.CharField(max_length=100)

    def __str__(self):
        return self.fuel


class Transmission(models.Model):
    transmission = models.CharField(max_length=100)

    def __str__(self):
        return self.transmission


class Car(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='cars_image')
    photo2 = models.ImageField(upload_to='cars_image', null=True, blank=True)
    photo3 = models.ImageField(upload_to='cars_image', null=True, blank=True)
    photo4 = models.ImageField(upload_to='cars_image', null=True, blank=True)
    desc = RichTextField()
    brand = models.ForeignKey(CarBrand, on_delete=models.PROTECT)
    body_type = models.ForeignKey(CarBody, on_delete=models.PROTECT)
    fuel_type = models.ForeignKey(FuelType, models.PROTECT)
    transmission = models.ForeignKey(Transmission, on_delete=models.PROTECT)
    price = models.PositiveIntegerField()
    interior_color = models.CharField(max_length=100)
    engine_name = models.CharField(max_length=100)
    mileage = models.PositiveIntegerField()
    km_driven = models.PositiveIntegerField()
    added_date = models.DateTimeField(auto_now=True)
    car_number = models.CharField(max_length=30)
    total_click = models.IntegerField(default=0, blank=True, null=True)
    is_blocked = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    is_price_negotiable = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CarWatchlist(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.PROTECT)
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    is_cart_visit = models.BooleanField(default=False)

    class Meta:
        unique_together = ['user', 'car']


class Comments(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.PROTECT)
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    date_of_added = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=1000)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.comment
