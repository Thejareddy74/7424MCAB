from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def  home(request):
    temp=loader.get_template('home.html')
    return HttpResponse(temp.render())

def green(request):
    stu=[{'name':'Theja','marks':90},{'name':'Neeraja','marks':85},
         {'name':'Dhanvi','marks':88},{'name':'Nandhu','marks':91}]

    return render(request,'green.html',{'data': stu})

def displaygreen(request):
    stu=['Theja','Neeraja','Dhanvi','Nandhu']
    return render(request,'displaygreen.html',{'data': stu})
 

