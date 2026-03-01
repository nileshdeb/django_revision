from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World!")
# Create your views here.

def about(request):
    a=10+20
    return HttpResponse("This is about page. The sum of 10 and 20 is: " + str(a))
