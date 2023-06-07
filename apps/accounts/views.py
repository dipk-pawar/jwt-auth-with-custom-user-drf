from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.accounts.serializers import (
    UserSerializers,
    LoginSerializers,
    UserProfileSerializers,
    UserChangePasswordSerializer,
    SendPasswordResetLinkEmailSerializer,
    ResetPasswordSerializer,
)
from rest_framework import status
from django.contrib.auth import authenticate
from jwt_auth_pr.jwt_custom_token import get_tokens_for_user
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
class RegisterUserAPIView(APIView):
    def post(self, request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            tokens = get_tokens_for_user(user=user)
            return Response(
                {"tokens": tokens, "message": "User registred successfully"},
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

        if user is None:
            return Response(
                {"errors": {"non_field_errors": ["Email or password is not valid"]}},
                status=status.HTTP_400_BAD_REQUEST,
            )

        tokens = get_tokens_for_user(user=user)
        return Response(
            {"tokens": tokens, "message": "Login successfully"},
            status=status.HTTP_200_OK,
        )


class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializers(request.user)
        return Response(
            {"data": serializer.data},
            status=status.HTTP_200_OK,
        )


class UserChangePassword(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = UserChangePasswordSerializer(
            data=request.data, context={"user": request.user}
        )
        if serializer.is_valid():
            return Response(
                {"message": "Password changed successfully"},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"errors": serializer.errors},
            )


class UserResetPasswordEmailLink(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SendPasswordResetLinkEmailSerializer(data=request.data)
        if serializer.is_valid():
            return Response(
                {
                    "data": serializer.data,
                    "message": "Reset password link sent to the email address",
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"errors": serializer.errors},
            )


class UserResetPassword(APIView):
    permission_classes = [AllowAny]

    def post(self, request, uid, token):
        serializer = ResetPasswordSerializer(
            data=request.data, context={"uid": uid, "token": token}
        )
        if serializer.is_valid():
            return Response(
                {"message": "Password reset successfully"},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"errors": serializer.errors},
                status=status.HTTP_200_OK,
            )
