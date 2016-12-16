"""sna_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from sentence import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^sentence/', views.sentence),
    url(r'^sentence_world/', views.sentence_world),
    url(r'^post_world/', views.post_world),
    url(r'^user/usermap/', views.usermap),
    url(r'^user/profile/', views.user_profile),
    url(r'^user/account/', views.user_account),
    url(r'^user/achievement/', views.user_achievement),
    url(r'^user/history/', views.user_history),
    #google+
    # url(r'^accounts/', include('allauth.urls')),
]
