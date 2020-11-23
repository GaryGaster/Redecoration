from django.urls import path
from .views import home, send_order_enquiry, authors


urlpatterns = [
    path('', home, name='home'),
    path('contact/', send_order_enquiry, name='contact'),
    path('authors/', authors, name='authors'),
]
