from django.urls import path
from . import  views

urlpatterns = [
    path('', views.link, name='link'),
    path('link_club/', views.link_club, name='link_club'),
    path('link_page/', views.link_page, name='link_page'),
]
