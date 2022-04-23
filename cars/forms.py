from ckeditor.fields import RichTextField
from django import forms

from accounts.models import MyUser
from .models import Car, CarBody, CarBrand


class CarBodyForm(forms.ModelForm):
    class Meta:
        model = CarBody
        fields = ['body_type']
        widgets = {
            'body_type': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CarBrandForm(forms.ModelForm):
    class Meta:
        model = CarBrand
        fields = ['brand']
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'user', 'photo', 'photo2', 'photo3', 'photo4', 'name', 'brand', 'body_type', 'fuel_type',
            'transmission',
            'price', 'interior_color', 'engine_name', 'desc', 'mileage', 'km_driven', 'car_number',
            'is_available', 'is_price_negotiable'
        ]
        labels = {
            'photo2': 'Photo 2 (Optional)',
            'photo3': 'Photo 3 (Optional)',
            'photo4': 'Photo 4 (Optional)',
        }
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'body_type': forms.Select(attrs={'class': 'form-control'}),
            'fuel_type': forms.Select(attrs={'class': 'form-control'}),
            'transmission': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),

            'interior_color': forms.TextInput(attrs={'class': 'form-control'}),
            'engine_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mileage': forms.NumberInput(attrs={'class': 'form-control'}),
            'km_driven': forms.NumberInput(attrs={'class': 'form-control'}),
            'car_number': forms.TextInput(attrs={'class': 'form-control'}),

        }

    def __init__(self, user, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        self.fields['user'].empty_label = None
        self.fields['user'].queryset = MyUser.objects.filter(email=user)
