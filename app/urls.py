from django.urls import path
from . import views

urlpatterns = [
        path('pres/', views.pres, name='pres'),
        path('madik/', views.madik, name='madik'),
        path('', views.test, name='test'),
        path('erd/', views.erd, name='erd'),
]
