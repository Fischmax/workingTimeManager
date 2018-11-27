from django.db import models


class Worktime(models.Model):
    # User-ID
    time_from = models.TimeField(default=None)
    time_to = models.TimeField(default=None)
    minutes_total = models.IntegerField(default=0)
    minutes_break = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)
    date = models.DateField(default=None)
