from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index , name="home"),
    path('profile/<int:id>', views.profile , name="profile"),
    path('profile/edit', views.edit , name="edit"),
]
