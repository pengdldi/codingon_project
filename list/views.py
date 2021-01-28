from django.shortcuts import render,redirect
from django.http.response import HttpResponse

# Create your views here.
def doit(request,uname):
    context = {'name1':uname}
    return render(request,'ver14.html',context)

