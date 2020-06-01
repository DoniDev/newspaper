from django.contrib import admin
from django.urls import path
from django.contrib.auth.models import User

urlpatterns = [
    path('admin/', admin.site.urls),
]
