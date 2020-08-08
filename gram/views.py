from django.shortcuts import render
from django.http HttpResponse

# Create your views here.
def welcome (request):
    return HttpResponse('welcome to the gram')

