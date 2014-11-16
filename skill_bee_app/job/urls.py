from django.conf.urls import patterns, url

from job import views

urlpatterns = patterns('',
    #url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^view-students/(?P<cat>\w+)/$', views.view_students , name='view_students'),
    url(r'^create-job/(?P<student_id>\w+)/$', views.create_job_request, name='create_job_request'),
)

