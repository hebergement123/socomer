"""monsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from typing import Pattern
from django.urls import include, path
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from hello_world.views import hello
urlpatterns = [
    
    path('admin/', admin.site.urls),
 
    path('',include('produit.urls')),
    #path('',include('login.urls')),
    #path('', hello_world),
    #path('', home),
    #path('accounts/', include('django.contrib.auth.urls')), # add
    #path('hello_world/', include('hello_world.urls'))
    
] 
urlpatterns += staticfiles_urlpatterns()

