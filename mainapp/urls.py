from django.conf.urls import url, include
from . import views
from django.conf import settings
urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^/$', views.login, name='login'),
    url(r'^createcoffee/', views.createCoffee, name='createcoffee'),
    url(r'^editcoffee/(?P<coffee_id>[0-9]+)/$', views.editCoffee, name='editcoffee'),

    url(r'^createbean/', views.createBean, name='createbean'),
    url(r'^editbean/(?P<bean_id>[0-9]+)/$', views.editBean, name='editbean'),

    url(r'^createpowder/', views.createPowder, name='createpowder'),
    url(r'^editpowder/(?P<powder_id>[0-9]+)/$', views.editPowder, name='editpowder'),

    url(r'^createsyrup/', views.createSyrup, name='createsyrup'),
    url(r'^editsyrup/(?P<syrup_id>[0-9]+)/$', views.editSyrup, name='editsyrup'),

    url(r'^createroast/', views.createRoast, name='createroast'),
    url(r'^editroast/(?P<roast_id>[0-9]+)/$', views.editRoast, name='editroast'),

    url(r'^createorder/(?P<coffee_id>[0-9]+)/$', views.createOrder, name='createorder'),


]
