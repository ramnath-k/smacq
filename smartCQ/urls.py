# yomamabot/fb_yomamabot/urls.py
from django.conf.urls import include, url
from .views import SmartCQView
urlpatterns = [
                 url(r'^chat/?$', SmartCQView.as_view()) 
               ]