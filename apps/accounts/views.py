from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.views import APIView
from apps.accounts.serializers import UserSerializers


# Create your views here.
class UserAPIView(APIView):
    def post(self, request):
        print(request.data)
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"msg": "hello"})
        else:
            return Response(serializer.error)
