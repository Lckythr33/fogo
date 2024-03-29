from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^logreg/$', views.logreg),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^update$', views.update),
    url(r'^donations$', views.donations),
    url(r'^account$', views.account),
    url(r'^admin_pg$', views.admin)
]