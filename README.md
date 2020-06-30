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

MANIPULER LE ROUTING

dans la vue de apptwo : création d'une fonction : 
def django_detail(request, category, year=0, month=0, day=0):
    body = "Category={}, year={}, month{}, day{}".format(category, year, month, day)
    return HttpResponse(body)
    
Celle-ci attend une categorie, une année (par défaut 0), un mois (par défaut 0), un jour (par défaut 0)
Elle retourne lors de la saisie de l'url les données : category, year, month et day

Pour ne pas surcharger le fichier urls.py nous allons en ajouter un dans apptwo. 
création des urls dans apptwo/urls.py :     
path('details/<str:category>/<int:year>/<int:month>/<dd:day>/', apptwo_views.django_detail),
Nous pouvons nettoyer également les lignes inutiles

création d'un fichier converters.py dans apptwo :
class TwoDigitDayConverter:
    # création d'une classe TwoDigitDayConverter

    regex = '[0-9]{2}'
    # création d'une petite regex : nous voulons des chiffres en 0 et 9 et nous en voulons 2

    def to_python(self, value):
        return int(value)
        # nous retournons un integer

    def to_url(self, value):
        return '%02d' % value
        # Nous retournons une valeur de 2 chiffres


ensuite dans apptwo/urls.py :

from django.urls import register_converter
# pour pouvoir enregistrer notre convertisseur dans le routing

from apptwo import converters

register_converter(converters.TwoDigitDayConverter, 'dd')



idem pour le fichier d'origine urls.py 
ajout de : path('apptwo/', include('apptwo.urls'))
ne pas oublier d'importer le include dans django.urls


url details : nous voulons du str pour category, du int pour year, month et day

Lorsque nous lançons le runserver il faut bien mettre le apptwo/ pour tomber sur les urls de apptwo

Maintenant nous avons deux fichiers urls.py mais ils sont moins chargés


