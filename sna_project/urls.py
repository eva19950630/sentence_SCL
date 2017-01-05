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
    url(r'^$', views.index,name="index"),
    # url(r'^sentence/', views.sentence),
    # url(r'^sentence_world/', views.sentence_world),
    # url(r'^post_world/', views.post_world),
    url(r'^user/usermap/', views.usermap),
    url(r'^user/profile/', views.user_profile),
    url(r'^user/account/', views.user_account),
    url(r'^user/achievement/', views.user_achievement),
    url(r'^user/history/', views.user_history),
    
    # url(r'^login/', views.signup_app),
    url(r'^login/', views.login_app),
    url(r'^sentence/translation/(?P<get_sid>\d+)/$', views.translation_post, name = 'translation_post'),
    url(r'^sentence_post/', views.sentence_post,name = 'sentence_post'),
    url(r'^sentence/(?P<sid>\d+)/$', views.sentence_url, name="sentence_url"),
    url(r'^user/profileIcon/', views.get_new_user_icon, name="get_new_user_icon"),
    # url(r'^likes/', views.likes_count, name="likes_count"),
    # url(r'^sentence_post/(?P<sid>\d+)/$', views.sentence_post,name = 'sentence_post'),
    url(r'^logout/', views.logout,name = "logout"),
    #fb
    url(r'^getuserid/', views.getuserid, name = 'getuserid'),
    #google+
    #url(r'^allauth/accounts/', include('allauth.urls')),
]
  
