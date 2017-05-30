from django.conf.urls import url, include
from . import views
from django.conf import settings
urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^i/$', views.login, name='login'),
]
