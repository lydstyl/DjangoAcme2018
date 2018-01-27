# from django.urls import include, path
from django.conf.urls import url

from . import views

urlpatterns = [
    # path('', views.home),
    # path('about/', views.about),
    url(r'^$', views.index),
    url(r'^posts/(?P<id>[0-9]+)$', views.show),
]