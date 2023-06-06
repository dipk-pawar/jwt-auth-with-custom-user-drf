from django.contrib import admin
from django.urls import path
from apps.accounts.views import UserAPIView

urlpatterns = [
    path("", UserAPIView.as_view(), name="accounts"),
]
