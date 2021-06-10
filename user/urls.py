from django.contrib import admin
from django.urls import path
from .api.apiview import UserRegisterView, UserLogin

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('login/', UserLogin.as_view()),
]