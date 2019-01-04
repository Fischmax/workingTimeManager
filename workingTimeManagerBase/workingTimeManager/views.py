import time
from MySQLdb import Date
from django.http import HttpResponse
from django.shortcuts import render
from .models import Worktime


def dashboard(request):

    return render(request, 'workingTimeManager/dashboard.html', {})


def add_time(request):
    # Check for input
    time_to_add = Worktime()
    time_to_add.date = Date.today()
    time_to_add.time_from = request.POST['time_from']
    time_from = time.strptime(time_to_add.time_from, '%H:%M')
    # print(time_to_add.time_from)
    time_to_add.time_to = request.POST['time_to']
    time_to = time.strptime(time_to_add.time_to, '%H:%M')
    if 'minutes_break' in request.POST:
        try:
            time_to_add.minutes_break = int(request.POST['minutes_break'])
        except ValueError:
            return HttpResponse(status=400)
    else:
        time_to_add.minutes_break = 45
    # print(time_to_add.time_to)
    if time_to < time_from:
        return HttpResponse(status=400)
    else:
        time_to_add.balance = (time_to.tm_hour*60 - time_from.tm_hour*60) + (time_to.tm_min - time_from.tm_min)
        time_to_add.minutes_total = time_to_add.balance + time_to_add.minutes_break
        time_to_add.balance = time_to_add.balance - (time_to_add.minutes_break + 8*60)
        # TODO: variable, automatic
        # print(time_to_add.balance)
        time_to_add.save()
        return HttpResponse('')
