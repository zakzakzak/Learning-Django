from django.conf.urls import url

from . import views

urlpatterns =[
    url(r'^$', views.index),

    url(r'^cerita/$', views.cerita),
    url(r'^news/$', views.news),
]
