from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # scrumboard urls
    url(r'^', include('board.urls')),

    # auth
    # url(r'^auth/', include('auth.urls')),

    # admin
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    from django.views.static import serve
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
            serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'^static/(?P<path>.*)$',
            serve, {'document_root': settings.STATIC_ROOT}),
        url(r'^favicon\.ico$',
            'django.views.generic.simple.redirect_to',
            {'url': '/static/images/favicon.ico'}),
    )