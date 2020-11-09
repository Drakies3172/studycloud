from django.shortcuts import render
from django.views.generic import TemplateView
from bookingsite.models import Hotel,Customer
from .form import CreateHotelForm,HomeForm,CreateBookingForm
from django.http import JsonResponse
from django.core import serializers



class Homeview(TemplateView):
    template_name = 'booked.html'
    template2_name = 'test.html'
    temp_array = ["","","","",""]
    def get(self,request):
        if request.method =="GET" and request.is_ajax():
            people = request.GET.get('people')
            self.temp_array[0] = people
            room = request.GET.get('room')
            self.temp_array[1] = room
            district = request.GET.get('district')
            self.temp_array[2] = district
            checkinDay = request.GET.get('checkinDay')
            self.temp_array[3] = checkinDay
            checkoutDay = request.GET.get('checkoutDay')
            self.temp_array[4] = checkoutDay
            hotelData = serializers.serialize("json", Hotel.objects.filter(district = district))
            return JsonResponse({"hotels": hotelData})
        return render(request,self.template2_name,{})
    def post(self,request):
        if request.method =="POST":
            name = request.POST.get('name')
            customer_id = request.POST.get('ID')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            inputAddress = request.POST.get('inputAddress')
            hotel = request.POST.get('hotel')
            district = request.GET.get('district')
            if len(self.temp_array) ==5:
                people = self.temp_array[0]
                room = self.temp_array[1]
                district = self.temp_array[2]
                checkInDay = self.temp_array[3]
                checkOutDay = self.temp_array[4]
                form = CreateBookingForm()
                newBooking = form.save(commit=False)
                newBooking.people = people
                newBooking.room = room
                newBooking.checkinday = checkInDay
                newBooking.checkoutday = checkOutDay
                newBooking.name = name
                newBooking.id_number = customer_id
                newBooking.email = email
                newBooking.phone = phone
                newBooking.current_address = inputAddress
                newBooking.hotel_name = hotel
                newBooking.save()
            arg = {"people":people,"room":room,"district":district,"checkInDay":checkInDay,"checkOutDay":checkOutDay,"name":name,"id":customer_id,
            "email":email,"phone":phone,"address":inputAddress,"hotel":hotel
            }
            

        return render(request,self.template2_name,{})
