from django.shortcuts import render,redirect
from .import forms

# Create your views here.
def add_category(request):
      if request.method=='POST':#User post request koreche // Post request mane holo Input field e data diyeche
            category_form=forms.CategoryForm(request.POST) #User er post request data eikhane catch korlam
            if category_form.is_valid():#post kora data valid naki check kortesi
                  category_form.save()#jodi data valid hoi database e save hoye jabe
                  return redirect('add_category')#Sob thik thakle add_author ei url a pathiye dibo
      

      else: #user normally ei site ta open korle blank form pabe
            category_form=forms.CategoryForm()
      return render(request,'add_category.html',{'form': category_form})
            