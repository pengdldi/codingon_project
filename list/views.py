from django.shortcuts import render,redirect
from django.http.response import HttpResponse

# Create your views here.
def doit(request,uname):
    context = {'welcome':uname}
    return render(request,'ver18.html',context)

def doit2(request):
    context = {}
    context['welcome'] = 'Welcome'
    return render(request,'ver18.html',context)

