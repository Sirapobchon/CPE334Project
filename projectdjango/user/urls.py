from django.urls import path,include
from .views import UserList

urlpatterns = [
    path('login/', UserList.login),
    path('register/', UserList.register),
]