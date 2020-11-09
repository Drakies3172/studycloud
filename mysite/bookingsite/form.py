from django import forms
from . import models
class HomeForm(forms.Form):
    name = forms.CharField()
    district = forms.CharField()
    capacity = forms.CharField()

class CreateHotelForm(forms.ModelForm):
    class Meta:
        model = models.Hotel
        fields = ['name','district','capacity']

class CreateBookingForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields =['people','room','checkinday','checkoutday','name',
        'id_number','email','phone','current_address','hotel_name'
        ]