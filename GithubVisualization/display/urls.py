from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^display1', views.display1, name = 'display1'),
    url(r'^display2', views.display2, name = 'display2'),
    url(r'^return_json', views.return_json, name = 'return_json'),
    url(r'^return_json_2', views.return_json_2, name = 'return_json_2'),
    url(r'^return_json_3', views.return_json_3, name = 'return_json_3'),
]