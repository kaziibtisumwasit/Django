#menually created in app
from django.urls import path
from . import views 
urlpatterns = [
    path('courses/', views.courses),#home page tai forword ba backword slash dewa lage nai
    path('about/', views.about),
    path("",views.home)
]
