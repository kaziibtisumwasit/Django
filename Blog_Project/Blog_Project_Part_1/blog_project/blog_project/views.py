from django.shortcuts import render
from posts.models import Post #posts app er models theke Post Class import korlam


def home(request):
      data = Post.objects.all() #Post class er joto object ache sob object data variable e chole ashbe
      print(data)
      return render(request,'home.html',{'data' : data})#data ke dictonary akare fornt-end e pathai dialm
