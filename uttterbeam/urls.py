from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uttterbeam.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index', 'main.views.index', name = 'index'),
    url(r'^author', 'main.views.author', name = 'author'),
    url(r'^post', 'main.views.post', name = 'post'),
)
