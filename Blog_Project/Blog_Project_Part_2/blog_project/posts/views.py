from django.shortcuts import render,redirect
from . import forms
from . import models

# Create your views here.
def add_post(request):
      if request.method =='POST':# jodi request method hoi tahole database e save howarr form ta 
            post_form = forms.PostForm(request.POST) #forms.py er PostForm Class
            if post_form.is_valid():
                  post_form.save()
                  return redirect('add_post') #save hower por urls.py file er add_post url er page ta show korbe
            
      else:#request method jodi normal hoi tahole blank form ta 
            post_form = forms.PostForm()
      return render(request,'add_post.html',{'form' : post_form})

def edit_post(request,id):
      post=models.Post.objects.get(pk=id) #models er Post Class er moddhe giye je id dewa hobe oi id er object post variable e store korlam
      
      #form ta te je input ghula ba data ghula chilo ta jate thake ba show kore forms er input field e 
      post_from=forms.PostForm(instance=post)
      #user ke je form ta dicchi edit er jonno oi form ti previous data ba details dara fillup kora thakbe


      if request.method == 'POST' :
            post_from = forms.PostForm(request.POST,instance=post)
            if post_from.is_valid():
                  post_from.save()
                  return redirect('homepage')
      # else:
      #       post_from=forms.PostForm()
      return render(request,'add_post.html',{'form' : post_from})




#delete oparation

def delete_post(request,id):
      post=models.Post.objects.get(pk=id) # database theke id diye oi post ta filter kore nilam ba dhorlam
      post.delete()
      return redirect('homepage')