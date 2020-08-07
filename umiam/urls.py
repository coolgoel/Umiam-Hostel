from django.urls import re_path
from . import views

app_name = 'umiam'

urlpatterns = [
        re_path('^$', views.index, name='index'),
        re_path('^gallery/$', views.hmc, name='galley'),
        re_path('^hmc-(?P<year>[0-9]+)/$', views.hmc, name='hmc'),
]

