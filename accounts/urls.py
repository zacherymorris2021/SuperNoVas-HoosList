# accounts/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.index, name='signup'),
    path('logout/', views.logout, name='logout'),
]
