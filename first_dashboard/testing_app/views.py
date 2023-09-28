from django.shortcuts import render
from django.http import HttpResponse

def testing_app(request):
    return HttpResponse("Hello world!")
