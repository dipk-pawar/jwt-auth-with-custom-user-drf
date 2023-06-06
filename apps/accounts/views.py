from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.accounts.serializers import UserSerializers, LoginSerializers
from rest_framework import status
from django.contrib.auth import authenticate


# Create your views here.
class UserAPIView(APIView):
    def post(self, request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"message": "User registred successfully"},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )


class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializers(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response(
                {"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )
        email = serializer.data.get("email")
        password = serializer.data.get("password")
        user = authenticate(email=email, password=password)
        return (
            Response(
                {"message": "Login successfully"},
                status=status.HTTP_200_OK,
            )
            if user is None
            else Response(
                {"message": "User not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        )
