# Created by Joshua de Guzman on 08/07/2018
# @email code@jmdg.io

from django.urls import path
from . import views
from .api import views

urlpatterns = [
    path('', views.AdvertisementList.as_view(), name='api_ads_list'),
]