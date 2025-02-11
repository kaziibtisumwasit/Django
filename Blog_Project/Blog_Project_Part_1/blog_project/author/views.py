from django.shortcuts import render,redirect

from . import forms
# Create your views here.
def add_author(request):
      #GET request e data ta url e show kore
      #POST request e data ta backend e thake

      if request.method == 'POST' :#request er vitor er method ta jodi post hoi
            author_form =forms.AuthorForm(request.POST) #USER form e data fillup korse dekhe request.POST nilam 
            #forms.py theke AuthorForm class ke niye ashlam
            if author_form.is_valid():#user je data pass korse oi data ghula valid kina 
                  author_form.save() #jodi valid hoi author er form ta save hoye jabe 
                  return redirect('add_author')
            #redirect mane form ta save howar por user ke kon page e pathabo
            #add_author page e paqthai dilam 
     



      #author_form.save() mane data ta database e save kora 


      #user jodi kono data input na dei just website ta visit korse 
      else:
             author_form = forms.AuthorForm()
             return render(request, 'add_author.html',{'form' : author_form})
      #front end e distonary er maddhome pass korlam author_form ke 
      #render hocche html templates & backend er data 

      


#user input field e data pass korle if kaj korbe 
#user jodi input e data pass na kore else kaj korbe
