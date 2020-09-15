"""blogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from users.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('posts.urls'),name='index'),
    path('home/',include('posts.urls'),name='home'),
    path('details/',include('posts.urls'),name='details'),
    path('delete/',include('posts.urls'),name='delete'),
    path('update/',include('posts.urls'),name='update'),
    path('view/',include('posts.urls'),name='view'),
    path('login/',Login_view,name='login'),
    path('register/',register_view,name='register'),
    path('logout/',logout_view,name='logout'),

]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

