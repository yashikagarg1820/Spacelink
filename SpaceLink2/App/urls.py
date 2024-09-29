from django.contrib import admin
from django.urls import path, include
from App import urls
from . import views
urlpatterns = [
    path('', views.index),
    path('index', views.index, name="index"),
    path('login', views.login, name="login"),
    path('registration', views.registration, name="registration"),
    path('booking', views.booking),
    path('profile', views.profile),
    path('about', views.about),
    # Planets
    path('sun', views.sun),
    path('moon', views.moon),
    path('mercury', views.mercury),
    path('venus', views.venus),
    path('earth', views.earth),
    path('mars', views.mars),
    path('jupiter', views.jupiter),
    path('saturn', views.saturn),
    path('uranus', views.uranus),
    path('neptune', views.neptune),
    path('pluto', views.pluto),
]
