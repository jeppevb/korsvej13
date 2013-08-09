# coding=UTF-8
import calendar
from django.core.serializers.json import json
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from models import Booking
from datetime import date, timedelta

def book(request):
    c = RequestContext(request, {"imagenums":range(1,22)})
    return render(request, "bookingformtable.html", c)

def home(request):
    c = RequestContext(request, {"imagenums":range(1,22)})
    return render(request, "index.html", c)

def booking(request, year, month):
    year = int(year)
    month = int(month)
    retval = []
    bookings = Booking.objects.filter(Q(firstday__range = (date(year, month, 1), date(year, month, calendar.monthrange(year, month)[1]))) | Q(lastday__range = (date(year, month, 1), date(year, month, calendar.monthrange(year, month)[1]))))
    for n in range(date(year, month, 1).weekday()):
        retval.append({"status":"unday", "day":""})
    for day in range(1,calendar.monthrange(year, month)[1]+1):
        mydate = date(year, month, day)
        if bookings.filter(firstday__lte = mydate).filter(lastday__gte = mydate).count() > 0:
            retval.append({"status":"booked", "day":mydate.strftime("%a") + " " + str(day) + "."})
        else:
            retval.append({"status":"open", "day":mydate.strftime("%a") + " " + str(day) + "."})
    while len(retval) < 35:
        retval.append({"status":"unday", "day":""})
    return HttpResponse(json.dumps(retval), mimetype="application/json")