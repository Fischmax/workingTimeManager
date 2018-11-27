from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    re_path('', include('workingTimeManager.urls')),
    path('admin/', admin.site.urls),
]
