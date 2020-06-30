from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def django_two(request):
    return HttpResponse("This is a Django apptwo")


def django_detail(request, category, year=0, month=0, day=0):
    template = loader.get_template('apptwo/index.html')
    return HttpResponse(template.render({}, request))

# création d'une vue qui retournera ce que l'utilisateur entrera dans l'url
