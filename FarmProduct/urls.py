from django.contrib import admin
from django.urls import re_path,include,path
from FarmProduct import views

app_name = 'FarmProduct'
urlpatterns = [

    re_path(r'^login/*$',           views.login),           # access: all
    re_path(r'^register/*$',        views.register),        # access: all

]
