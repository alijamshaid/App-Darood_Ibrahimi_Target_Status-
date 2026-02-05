from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from mydarood.models import todaydata
from datetime import date
from django.db.models import Sum
from django.http import JsonResponse
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from django.db.models import F


# Create your views here.

def todaydarood(request):
    if request.method == "POST":
        name = request.POST.get('name')
        print(name)
        recited = request.POST.get('recited')
        print(recited)
        date = request.POST.get('eventDate')
        print(date)
        data = todaydata(name=name,recited=recited,eventDate=date)
        data.save()
    return render(request, "todaydarood.html")

def statistics(request):
    totSum = todaydata.objects.aggregate(Sum('recited'))
    remaining=10000000-totSum['recited__sum']
    allRows = todaydata.objects.all()
    totalRows = todaydata.objects.all().count()
    context = {
        'remaining': remaining,
        'allRows': allRows,
        'totalRows':totalRows,
        'totSum' : totSum['recited__sum'],
        'naikiGatal' : totSum['recited__sum'] * 10,
        'gunahMaaf' : totSum['recited__sum']*10,
        'darajatBuland' : totSum['recited__sum']*10,
    }
    return render(request,"statistics.html",context)

def counter(request):
    if request.method == "POST":
        ajjDate=date.today()
        # name = request.POST.get('location')
        countdarood = request.POST.get('counteradded')
        print(countdarood)
        ajjDarood = todaydata.objects.filter(eventDate=ajjDate).values('eventDate')
        if(len(ajjDarood)==0):
            data = todaydata(name="Muhammad Ali",recited=countdarood,eventDate=date.today())
            data.save()
        else:
            todaydata.objects.filter(eventDate=ajjDate).values('eventDate').update(recited=F('recited') + countdarood)
        return render(request,"counter.html")
    else:
        return render(request,"counter.html")
    

def counter2(request):
    if request.method == "POST":
        name = request.POST.get('location')
        geolocator = Nominatim(user_agent="my_geocoding_app",timeout=10)
        try:
            spatialLocation = geolocator.geocode(name)
            latitude = spatialLocation.latitude
            longitude = spatialLocation.longitude
            context = {
                "spatialLatitude" : latitude,
                "spatialLongitude": longitude,
            }
            return render(request,"counter.html",context)
        except:
            return render(request,"counter.html")
    else:
        return render(request,"counter.html")

