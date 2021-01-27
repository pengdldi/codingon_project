from django.shortcuts import render,redirect
from django.http.response import HttpResponse

# Create your views here.
def doit(request):
    return render(request,'ver6.html')

