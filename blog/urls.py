from django.urls import path
from . import  views

urlpatterns = [
    path('', views.listing, name='blog'),
    path('<int:pk>', views.post, name='post'),
    path('delete/<int:pk>', views.delete_post, name='delete'),
    path('delete/comment/<int:pk>', views.delete_comment, name='delete_comment'),
]
