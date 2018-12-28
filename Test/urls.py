"""Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from Zawarudo import views
from django.conf.urls import include
from django.conf.urls import static
from Test import settings
#定义url
urlpatterns = [
    path(r'admin/', admin.site.urls),
    #path('home/', views.index),
    path(r'Zawarudo/', include('Zawarudo.urls')),
]

#打包时用于复制文件
urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
