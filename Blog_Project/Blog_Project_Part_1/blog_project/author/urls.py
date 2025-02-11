from django.contrib import admin
from django.urls import path,include
from . import views
#oi add author page er url er nam dilam add _author .nexttime theke ei num er url ti call korbo
urlpatterns = [
    path('add/',views.add_author,name='add_author'),
]
