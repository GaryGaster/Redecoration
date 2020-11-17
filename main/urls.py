from django.urls import path
from .views import home, send_order_enquiry


urlpatterns = [
    path('', home, name='home'),
    path('contact/', send_order_enquiry),
]
