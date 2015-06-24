from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.index'),
    url(r'^article/(?P<id>\d+)/$', 'blog.views.detail'),
    url(r'^login/$', 'blog.views.login'),
    url(r'^admin/$', 'blog.views.login_verify'),
    url(r'^article/new/$', 'blog.views.article_new'),
    url(r'^article/edit/(?P<id>\d+)/$', 'blog.views.article_edit'),
    url(r'^article/del/(?P<id>\d+)/$', 'blog.views.article_del'),
)

urlpatterns += static(settings.STATIC_URL,
        document_root=settings.STATIC_ROOT)
