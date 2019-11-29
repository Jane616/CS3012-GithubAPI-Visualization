from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^export1', views.export1, name = 'export1'),
    url(r'^export23', views.export23, name = 'export23'),
]