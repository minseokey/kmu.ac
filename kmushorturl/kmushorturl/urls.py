"""kmushorturl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include
import coreapp.views

urlpatterns = [
    path('admin/login/', coreapp.views.not_found, name='not_found'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('mypage', coreapp.views.mypage, name='mypage'),
    path('not_found', coreapp.views.not_found, name='not_found'),
    path('api/create', coreapp.views.create, name='create'),
    path('api/edit', coreapp.views.edit, name='edit'),
    path('api/delete', coreapp.views.delete, name='delete'),
    path('<str:path_word>/qrcode', coreapp.views.qr, name='qrcode'),
    path('', coreapp.views.index, name='index'),
    path('<str:path_word>', coreapp.views.mapping, name='mapping')
]
