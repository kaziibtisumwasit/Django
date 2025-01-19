#logical kaj gula views.py te hobe

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def courses(request):
      return HttpResponse("This is first_app/ Courses Page")
def about(request):
      return HttpResponse("This is first_app/ About Page")

def home(request):
      return HttpResponse("This is first_app/ Home Page")      