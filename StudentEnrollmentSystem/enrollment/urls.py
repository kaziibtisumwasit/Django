from django.urls import path
from . import views

urlpatterns = [
    path('', views.enrollment_list, name='enrollment_list'),
    path('add/', views.add_enrollment, name='add_enrollment'),
]
