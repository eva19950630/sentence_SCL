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
from django.conf import settings
from django.conf.urls.static import static

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
    url(r'^user/collection/', views.user_collection),
    url(r'^user/history/', views.user_history),
    url(r'^user/friends/', views.user_friends),
    
    # url(r'^login/', views.signup_app),
    url(r'^login/', views.login_app),
    url(r'^search/(?P<ranktype>\d+)', views.search,name="search"),
    url(r'^sentence/translation/(?P<get_sid>\d+)/$', views.translation_post, name = 'translation_post'),
    url(r'^get/translation/(?P<sid>\d+)/$', views.get_translation, name = 'get_translation'),
    url(r'^sentence_post/', views.sentence_post,name = 'sentence_post'),
    url(r'^sentence/(?P<sid>\d+)/$', views.sentence_url, name="sentence_url"),
    url(r'^user/profileIcon/', views.get_new_user_icon, name="get_new_user_icon"),
    url(r'^likes/', views.likes_count, name="likes_count"),
    url(r'^translation_likes/', views.transltion_likes_count, name="translation_likes_count"),
    url(r'^collect/', views.collection, name="collect"),
    # url(r'^sentence_post/(?P<sid>\d+)/$', views.sentence_post,name = 'sentence_post'),
    url(r'^logout/', views.logout,name = "logout"),
    #fb
    # url(r'^getuserid/', views.getuserid, name = 'getuserid'),
    url(r'^getcountry/', views.getCountry, name = 'getcountry'),
    url(r'^getregion/', views.getregion, name = 'getregion'),
    url(r'^addfriend/', views.addfriend, name = 'addfriend'),
    #google+
    #url(r'^allauth/accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)