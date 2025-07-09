from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def demo(request):
    temp=loader.get_template('headingtags.html')
    return HttpResponse(temp.render())