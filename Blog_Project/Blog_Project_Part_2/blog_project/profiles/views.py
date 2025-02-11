from django.shortcuts import render,redirect #redurect er kaj holo form submit er por kon page e jabe
#render er kaj holo front-end er file render b show kora browser e
from . import forms # ei app er forms.py te ja ache sob import korlam 

# Create your views here.
def add_profile(request):
      if request.method == 'POST':
            profile_form=forms.ProfileForm(request.POST)
            if profile_form.is_valid():
                  profile_form.save()#profile_form jodi valid hoi database e save hobe
                  return redirect('add_profile')
            
      else:
                  profile_form = forms.ProfileForm()
      return render(request,'add_profile.html',{'form' : profile_form})


