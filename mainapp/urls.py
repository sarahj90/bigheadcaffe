from django.conf.urls import url, include
from . import views
from django.conf import settings
urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^/$', views.login, name='login'),
    url(r'^createcoffee/', views.createCoffee, name='createcoffee'),
    url(r'^editcoffee/(?P<coffee_id>[0-9]+)/$', views.editCoffee, name='editcoffee'),

]
