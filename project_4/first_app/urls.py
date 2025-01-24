from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='home'),#1st er runserver er je url ta chilo oi url ke home url diye rename kore dilam

#     path('about/',viwes.about,name='about'),#about url ta create kore dilam
    path('about/',views.about, name='about'),#about url ta create kore dilam
    #viwes theke about function ti call korlam & about page er url ta ke about nam e rename kore dilam
]

#about/<int:id>/   ==> er mane holo url e ki show korbe eta
#about er path e int value nicchi ja 
#path mane je link ta website e url bar e show hoi oi link ta ke path e bole
#mane oi page ba site ta ei path e ache