from django.conf.urls import url,include
from django.contrib import admin

from . import views
from about import views as aboutViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),

    # nyambung ke blog
    # gak dikasih $ karena akan nyambung ke file blog
    # sehingga menjadi 'home' nya blog
    url(r'^blog/', include('blog.urls')),

    # menuju page app (about)
    url(r'^about/$', aboutViews.index),
]
