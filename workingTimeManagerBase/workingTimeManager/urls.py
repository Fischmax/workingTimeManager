from django.urls import re_path
from . import views

urlpatterns = [
    re_path('^add_time/$', views.add_time, {}),
    re_path('', views.dashboard, {}),
]
