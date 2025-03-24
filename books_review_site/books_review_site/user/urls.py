from django.urls import path
from user.views import register_user, logout_user
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("register", register_user, name='register'),
    path("login", LoginView.as_view(), name='login'),
    path("logout", logout_user, name='logout'),
]