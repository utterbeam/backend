from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uttterbeam.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'main.views.index2', name = 'home'),
    
    url(r'^author/(?P<username>[\*\w\-]+)$', 'main.views.authorF', name = 'author'),
    # url(r'^post$', 'main.views.post', name = 'post'),
    
    # url(r'^login$', 'main.views.facebook_login', name = 'fblogin'),
    
    url(r'^upload$', 'main.views.upload', name = 'upload'),
    
    # url(r'^logged_in$', 'main.views.index', name = 'index'),
    
    url(r'^uploadWriteup$', 'main.views.uploadWriteup', name = 'uploadWriteup'),
    
    url(r'^post/(?P<uid>[\*\w\-]+)$' ,'main.views.post' , name = 'post'),
    
    url(r'^login/$', 'main.views.login', name='login'),
    
    url(r'^logout/$', 'main.views.logout', name='logout'),
    
    url(r'^oauth/', include('social_django.urls', namespace='social')),

    url(r'^signup/$', 'main.views.signup', name='signup'),



)

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'