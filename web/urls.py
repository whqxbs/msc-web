from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/',views.login),
    path('logout/',views.logout),
    path('register/',views.register),
    path('tests/',views.tests)
]
