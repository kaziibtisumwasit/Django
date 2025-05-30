from django.shortcuts import render

import datetime #import datetime module to get date & time 

# Create your views here.


def index(request):
      d={'lst':['a','b','c','d','e'],'name':'Rahul','age':20,'date': datetime.datetime.now(),
         'student' : [
    {'name': 'Josh', 'age': 19},
    {'name': 'Dave', 'age': 22},
    {'name': 'Joe', 'age': 31},
],'empty':'','t': datetime.datetime.now().time(),'old_date':datetime.datetime(2022,12,1),'event' : datetime.datetime(2024,10,4),'post_time' : datetime.datetime(2022,3,24,14,30,45 ),'comment_time' : datetime.datetime(2024,11,3,12,30,45),'st': "hello world Happy Coding "}
      #'date' : datetime.datetime.now() is use to get the current date & time 
      #for only date need datetime.date.today() or datetime.dateime.now().date()
      #if you want only time then use datetime.datetime.now().time()
      #datetime(year , month ,day, hour, minute ,second, microsecond)
      
      return render(request,'index.html',d)