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
