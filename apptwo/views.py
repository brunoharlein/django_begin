from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def django_two(request):
    return HttpResponse("This is a Django apptwo")