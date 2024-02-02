
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('repair', views.repair, name='repair'),
    path('shop', views.shop, name='shop'),
    path('delivery', views.delivery, name='delivery'),
    path('reviews', views.reviews, name='reviews'),
    
    path('contact', views.contact, name='contact')
]
