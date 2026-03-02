from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_01(requests):
    return HttpResponse("I am revising Django Concepts!")

def hello_02(request):
    return render(request, 'hello.html', {'name': 'Abubakar'}) 

# For Debugging Purpose
def hello_03(request):
    x = 2
    y = 3
    return HttpResponse(f"The sum of {x} and {y} is: {x+y}")