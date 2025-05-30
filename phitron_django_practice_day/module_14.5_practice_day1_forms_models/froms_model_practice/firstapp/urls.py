from django.urls import path
from .import views

urlpatterns = [
    path('',views.app_index , name='appindex'),
    path('add_forms/',views.addforms,name='addforms'),
    path('add_model_form/',views.StudentModel,name='studentModel')
]
