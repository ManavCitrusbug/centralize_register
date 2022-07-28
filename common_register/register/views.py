from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView
from register.models import *
from rest_framework.permissions import AllowAny,IsAuthenticated
from register.serializer import *
from register.models import *
from django.contrib.auth.models import  auth

from rest_framework_simplejwt.views import TokenObtainPairView




class Userprofile(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class=Registerserializer
    def get_object(self):

        return self.request.user
         

class Registerapi(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class=Registerserializer
    permission_classes=[AllowAny]


