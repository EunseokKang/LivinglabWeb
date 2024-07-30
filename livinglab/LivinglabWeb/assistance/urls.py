from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('psy-1', views.psy_1, name='psy-1'),
    path('psy-2', views.psy_2, name='psy-2'),
    path('psy-3', views.psy_3, name='psy-3'),
    path('eco-1', views.eco_1, name='eco-1'),
    path('eco-2', views.eco_2, name='eco-2'),
    path('eco-3', views.eco_3, name='eco-3'),
    path('eco-4', views.eco_4, name='eco-4'),
    path('eco-5', views.eco_5, name='eco-5'),
    path('eco-6', views.eco_6, name='eco-6'),
    path('eco-7', views.eco_7, name='eco-7'),
    path('eco-8', views.eco_8, name='eco-8'),
    path('eco-9', views.eco_9, name='eco-9'),
    path('law-1', views.law_1, name='law-1'),
    path('law-2', views.law_2, name='law-2'),
    path('law-3', views.law_3, name='law-3'),
    path('law-4', views.law_4, name='law-4'),
    path('law-5', views.law_5, name='law-5'),
    path('law-6', views.law_6, name='law-6'),
    path('int-1', views.int_1, name='int-1'),
    path('int-2', views.int_2, name='int-2'),
    path('int-3', views.int_3, name='int-3'),
    path('int-4', views.int_4, name='int-4'),
    path('int-5', views.int_5, name='int-5'),
    path('int-6', views.int_6, name='int-6'),
    path('int-7', views.int_7, name='int-7'),
]