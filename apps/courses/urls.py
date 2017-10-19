from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="courses"),
    url(r'^add_course$', views.add_course, name="add_course"),
    url(r'^courses/(?P<id>\d+)/remove_request$', views.remove_request, name="remove_request"),
    url(r'^courses/(?P<id>\d+)/remove$', views.remove, name="remove_sure") 
]