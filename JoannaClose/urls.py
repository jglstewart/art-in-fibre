from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'JoannaClose.views.home', name='home'),
    # url(r'^JoannaClose/', include('JoannaClose.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

(r'^$', 'blog.views.index'),
url(
    r'^blog/view/(?P<slug>[^\.]+)', 
    'blog.views.view_post', 
    name='view_blog_post'),
url(
    r'^about.html', 
    'blog.views.view_about', 
    name='view_about'),
url(
    r'^gallery/(?P<page>\d+)', 
    'blog.views.view_gallery', 
    name='view_gallery'),
url(
    r'^gallery/(?P<slug>[^\.]+)', 
    'blog.views.view_product', 
    name='view_gallery_product'),
url(
    r'^blog/(?P<page>\d+)', 
    'blog.views.view_blog', 
    name='view_blog'),
url(
    r'^blog/category/(?P<slug>[^\.]+)/(?P<page>\d+)', 
    'blog.views.view_by_category', 
    name='view_by_category'),
url(
    r'^contact.html', 
    'blog.views.view_contact', 
    name='view_contact'),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT}))
