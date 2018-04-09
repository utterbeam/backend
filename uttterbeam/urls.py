from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uttterbeam.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.index2', name = 'index2'),
    url(r'^author', 'main.views.author', name = 'author'),
    url(r'^post', 'main.views.post', name = 'post'),
    url(r'^login', 'main.views.login', name = 'login'),
    url(r'^upload', 'main.views.upload', name = 'upload'),
    url(r'^logged_in', 'main.views.index', name = 'index'),
)
