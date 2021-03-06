# Generated by Django 2.0.1 on 2018-11-27 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workingTimeManager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worktime',
            name='balance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='worktime',
            name='date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='worktime',
            name='minutes_break',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='worktime',
            name='minutes_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='worktime',
            name='time_from',
            field=models.TimeField(default=None),
        ),
        migrations.AddField(
            model_name='worktime',
            name='time_to',
            field=models.TimeField(default=None),
        ),
    ]
