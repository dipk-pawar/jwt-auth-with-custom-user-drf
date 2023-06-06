from django.contrib import admin
from django.urls import path
from apps.accounts.views import UserAPIView, LoginAPIView

urlpatterns = [
    path("", UserAPIView.as_view(), name="accounts"),
    path("login/", LoginAPIView.as_view(), name="login"),
]
