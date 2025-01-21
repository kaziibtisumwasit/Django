
from django.shortcuts import render#render ke import korte hobe


def home(request):#home ekti function perameter hishbe request ashbe
      return render(request,'home.html')
#render hobe request,template er moddhe thaka html file