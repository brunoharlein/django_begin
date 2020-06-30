1) Lancer Pycharm (création de projet)
2) Nom du projet + validation de la version de Python

3) Terminal : pip install Django
4) django-admin startproject begin_django . 

5) test du projet : Terminal : python manage.py runserver (ctrl + c pour finir)

6) Création d’une app dans notre projet : python manage.py startapp apponetest

7) Dans begin_django/setting.py
INSTALLED_APPS = ‘apponetest.apps.ApponetestConfig’,

8) Dans views.py
from django.http import HttpReponse

def hello(request):
	return HttpResponse(“Hello”)

9) Dans urls.py
from appone import views
path(‘hello/’, views.hello)      hello = nom de la fonction

10) python manage.py runserver ==) mettre /hello lors de l’adresse.

Exemple (exo)
    - créer une app Django apptwo 
    - une route, une vue et afficher la réponse "This is a Django apptwo"
    
1) python manage.py startapp apptwo
2) settings.py =) 'apptwo.apps.ApptwoConfig',
3) urls =) from apptwo import views as apptwo_views
           path('django_two/' apptwo_views.django_two)
4) faire alt + entrée pour choisir "create function django_two"
5) views.py de apptwo : from django.http import HttpResponse
6) ajout du parametre (request)
7) return HttpResponse("This is a Django apptwo")
8) Terminal : python manage.py runserver
9) Ajoute django_two/ à la suite de l'adresse

