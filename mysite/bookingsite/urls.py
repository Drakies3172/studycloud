from django.conf.urls import url
from bookingsite.views import Homeview
urlpatterns = [
    url(r'^$',Homeview.as_view(),name= 'view'),
]
 