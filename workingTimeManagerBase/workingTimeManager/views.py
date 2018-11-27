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
    # print(time_to_add.time_to)
    if time_to < time_from:
        return HttpResponse(code=400)
    else:
        time_to_add.balance = (time_to.tm_hour*60 - time_from.tm_hour*60) + (time_to.tm_min - time_from.tm_min)
        time_to_add.minutes_break = 45
        time_to_add.balance -= time_to_add.minutes_break
        # TODO: variable, automatic
        # print(time_to_add.balance)
        time_to_add.save()
        return HttpResponse('')
