"""my_first_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import *
from my_first_site.views import hello, hours_ahead, current_datetime, jodel
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
               url(r'^jodel/$', jodel),
               url(r'^hello/$', hello),
               url(r'^time/$', current_datetime),
               url(r'^time/plus/(\d{1,2})/$', hours_ahead)
               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
