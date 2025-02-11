from django.shortcuts import render


data=[
    {
        'name': 'Liam',
        'age': 27,
        'city': 'New York'
    },
    {
        'name': 'Sofia',
        'age': 22,
        'city': 'Madrid'
    },
    {
        'name': 'Amir',
        'age': 31,
        'city': 'Dubai'
    },
    {
        'name': 'Aya',
        'age': 29,
        'city': 'Tokyo'
    },
    {
        'name': 'Pierre',
        'age': 34,
        'city': 'Paris'
    },
]



# Create your views here.
def index(request):
      return render(request,'index.html',{"data":data})
#backend theke frontend e data pathanor somoy distonary maddhome pathano hoi
#data is a list of dictionary
#so mainly data is a list
#then I have a data which is list.I put this data in a disctonary which key is data