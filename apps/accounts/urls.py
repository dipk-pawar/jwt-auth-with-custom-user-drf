from django.contrib import admin
from django.urls import path
from apps.accounts.views import (
    RegisterUserAPIView,
    LoginAPIView,
    UserProfileAPIView,
    UserChangePassword,
)

urlpatterns = [
    path("register/", RegisterUserAPIView.as_view(), name="accounts"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("user-profile/", UserProfileAPIView.as_view(), name="user_profile"),
    path("change-password/", UserChangePassword.as_view(), name="change_password"),
]
