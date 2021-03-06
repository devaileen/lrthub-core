"""lrthubcore URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('api/v1/token/generate', obtain_jwt_token),
    path('api/v1/token/refresh', refresh_jwt_token),
    path('api/v1/token/verify', verify_jwt_token),
    path('api/v1/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/feeds/', include('feeds.urls')),
    path('api/v1/feedback/', include('feedback.urls')),
    path('api/v1/ratings/', include('ratings.urls')),
    path('api/v1/company/', include('company.urls')),
    path('api/v1/ads/', include('ads.urls')),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/traincheck/', include('traincheck.urls')),
    path('faqs/', include('faqs.urls')),
    url(r'^admin/', admin.site.urls),
]
