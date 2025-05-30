from django.urls import path
from firstapp.views import index# . mane current directory ba carently je folder er  moddhe achi 


urlpatterns =[
      path('',index,name='index'),
]