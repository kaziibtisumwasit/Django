from django.urls import path,include#import korbo include ke
from . import views
urlpatterns = [
    path('about/',views.about),
    path('contact/',views.contact),
#     path('navigation/',include('navigation.urls')),
    # site er about page e jete about/ diye jabo,function call hobe views file er about function
    #include navigation er moddhe urls ke include korbo,mane app er urls ke
    #navigation(app) er moddhe joto urls create korbo sob start hobe navigation\ diye

]