from django.contrib import admin
from django.urls import path,include
from mydarood import views

urlpatterns = [
    path('todaydarood',views.todaydarood,name='today darood'),
    path('statistics',views.statistics,name='statistics'),
    path('counter',views.counter,name='counter'),
    path('counter2',views.counter2,name='counter2'),
]