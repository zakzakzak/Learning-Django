from django.conf.urls import url
from django.contrib import admin

from . import views
from blog import views as blogViews
from about import views as aboutViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),

    # menuju page app (blog)
    url(r'^blog/$', blogViews.index),

    # menuju page app (about)
    url(r'^about/$', aboutViews.index),
]
