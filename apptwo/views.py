from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def django_two(request):
    return HttpResponse("This is a Django apptwo")

def django_detail(request, category, year=0, month=0, day=0):
    body = "Category={}, year={}, month{}, day{}".format(category, year, month, day)
    return HttpResponse(body)

# création d'une vue qui retournera ce que l'utilisateur entrera dans l'url