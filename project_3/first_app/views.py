from django.shortcuts import render
import datetime #date time ke import korlam

# Create your views here.


def home(request):
      #must be given in dictonary format
      d={'author' : 'Rahim','age' : 5,'lst':[1,2,3,4,5,6],'courses' : [{
            'id':1,
            'name' : 'python',
            'fees' : 5000,
            'duration' : 3
      }
      ,{
            'id':2,
            'name' : 'java',
            'fees' : 6000,
            'duration' : 4
      },
      {
            'id':3,
            'name' : 'c++',
            'fees' : 4000,
            'duration' : 2
      }]
      ,'word':['Python','Is','Boss'],'birthdate' : datetime.datetime.now()
      ,'val':''
      
      }
      
      #this is backend data
      #this backend data want to pass or render on front-end
      return render(request,'home.html',d)#d dictonary ke pass kore dilam
#another way to pass d data
#return render(request,'home.html',{'author' : 'rahim',age:20})
#onemore another way
#return render(request,'home.html',contex=d)EDIUS