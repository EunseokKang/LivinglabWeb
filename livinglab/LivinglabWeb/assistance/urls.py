from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('psy-1', views.psy_1, name='psy-1'),
]