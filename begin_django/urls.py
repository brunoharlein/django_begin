"""begin_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from apponetest import views
from apptwo import views as apptwo_views
# import de mon app et sa vue en alias ici

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('django_two/', apptwo_views.django_two),
    # création de l'url puis alt + entrée pour faire directement une création de function dans la vue
]
