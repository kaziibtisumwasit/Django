from django.shortcuts import render,redirect
from .forms import StudentForms

from . models import  Studentmodel


# Create your views here.

def app_index(request):
      return render(request,'appindex.html')


def addforms(request):
      if request.method == 'POST':
            form=StudentForms(request.POST)
            if form.is_valid():
                  print(form.cleaned_data)
                  return render(request,'form_success.html',{'data' : form.cleaned_data })
      
      else :
            empty_form=StudentForms
            return render(request,'forms.html',{'form' : empty_form})
      
def StudentModel(request):
      students = Studentmodel.objects.all()
      print(students)
      return render(request,'modelForm.html',{'model_data' : students})

