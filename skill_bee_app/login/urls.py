from django.conf.urls import patterns, url

from login import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register-student/$', views.register_student, name='register_student'),
    url(r'^register-client/$', views.register_client , name='register_client'),
)

