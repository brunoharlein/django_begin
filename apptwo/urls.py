from django.urls import path

from apptwo import views as apptwo_views
# import de mon app et sa vue en alias ici

from django.urls import register_converter
# pour pouvoir enregistrer notre convertisseur dans le routing

from apptwo import converters

register_converter(converters.TwoDigitDayConverter, 'dd')


urlpatterns = [
    path('django_two/', apptwo_views.django_two),
    # création de l'url puis alt + entrée pour faire directement une création de function dans la vue
    path('details/<str:category>/', apptwo_views.django_detail),
    path('details/<str:category>/<int:year>/', apptwo_views.django_detail),
    path('details/<str:category>/<int:year>/<int:month>/', apptwo_views.django_detail),
    path('details/<str:category>/<int:year>/<int:month>/<dd:day>/', apptwo_views.django_detail),

]
