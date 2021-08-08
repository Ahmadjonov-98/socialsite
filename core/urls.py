"""core URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from core.views import HomePage, TestPage, ThanksPage
from django.contrib.auth import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls', namespace='account')),
    path('account/', include('django.contrib.auth.urls')),
    path('group/', include('group.urls',namespace='group')),
    path('post/', include('post.urls',namespace='post')),
    path('test/',TestPage.as_view(),name='test'),
    path('thanks/',ThanksPage.as_view(),name='thanks'),
    path('', HomePage.as_view(), name='home'),

]
