from django.shortcuts import render


data=data = [
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
    }
]

# Create your views here.
def index(request):
      return render(request,'index.html')