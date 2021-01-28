from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
        path('', views.doit2, name='doit2'),
        path('<str:uname>/', views.doit, name='doit')
]

