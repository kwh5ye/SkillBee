from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^auth/', include('auth_op.urls')),
    url(r'^job/', include('job.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
