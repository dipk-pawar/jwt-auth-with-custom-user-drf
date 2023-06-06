from rest_framework import serializers
from apps.accounts.models import User


class UserSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"})

    class Meta:
        model = User
        fields = ["email", "name", "phone_no", "password", "password2", "is_tc"]

    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("password2")
        if password != confirm_password:
            raise serializers.ValidationError("Password didn't matched")
        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


class LoginSerializers(serializers.ModelSerializer):
    email = serializers.CharField(max_length=50)

    class Meta:
        model = User
        fields = ["email", "password"]
