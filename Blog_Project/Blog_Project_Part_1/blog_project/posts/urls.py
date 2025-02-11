from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns=[
      path('add/',views.add_post,name='add_post'),
      # add post er page er url path define korlam add/-->post/add/
      # views.py er add_post function ta call hobe
      # ei post page er url ba add port er url ke ekta nick name or ekta name dilam add_post
      # next time theke ei url ke ei name diye call korbo

      path('edit/<int:id>',views.edit_post,name='edit_post'),
      path('delete/<int:id>', views.delete_post,name='delete_post')

]