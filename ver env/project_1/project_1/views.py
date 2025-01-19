#project e views thake na 
#views menually add korte hoi
#ekti app project chara ochol

from django.http import HttpResponse


def home(request):
    return HttpResponse("This is main home Page")
def contact(request):
    return HttpResponse("This is Contact Page")
