from django.shortcuts import render
from django.http import HttpResponse#Http response ke django http theke import korte hobe
# Create your views here.
#URL jokhon hit kora hoi oi url ta ba oi request ta views er moddhe ashe,then views oi request ta accept kore,accept korar por ekta response return kore   
def home(request):
      #shey response ti holo Http response
      # return HttpResponse("This is Home Page Of First_app/")
      # return render('')
      return render(request,'first_app/home.html')
