from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('This is the home page') 


def second(request):
    return HttpResponse('Welcome to the second page') 


def third(request):
    return HttpResponse('blue green bluuuueeeee') 


def fourth(request):
    return HttpResponse('I would like some pizza') 