# -*- coding: utf-8 -*-
"""coodise URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import main
from .views import login
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls, name="admin"),
    url(r'^login/(?P<redirect_to>.*)$', login.Login.as_view(), name="login"),
    url(r'^logout/', login.Logout.as_view(), name="logout"),
    url(r'path/(?P<look_path>.*)/$', main.List.as_view(), name="path"),
    url(r'file/(?P<file_name>.*)/$', main.Serve.as_view(), name="file_server"),
    url(r'path/$', main.List.as_view(), {"look_path": "."}, name='index'),
    # url(r'path/$', RedirectView.as_view(url="/"), name="index"),
    url(r'^$', main.List.as_view(), {"look_path": ""}, name="index")
]
urlpatterns += staticfiles_urlpatterns()
