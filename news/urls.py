
from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    # path('1', views.bootstrap, name='bootstrap'),
    # path('2', views.b2, name='2'),

]




