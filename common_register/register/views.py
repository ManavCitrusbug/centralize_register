

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
from urllib import response
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import stripe
from common_register.settings import *

# from models import *
import json
stripe.api_key=STRIPE_SECRET_KEY

class Customer(View):
    def get(self,request,*args, **kwargs):
        description=request.GET.get('description')
        balance=int(request.GET.get('balance'))
        email=request.GET.get("email")
        phone=int(request.GET.get("phone"))

        customer = stripe.Customer.create(
            description=description,
            balance=balance,
            email=email,
            phone=phone
        )
        cus=stripe.Customer.retrieve(customer.id)
        y = json.dumps(cus)
        print(y["id"])
        
        return JsonResponse({"customer":customer})



class Userprofile(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class=Registerserializer
    def get_object(self):

        return self.request.user
         

class Registerapi(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class=Registerserializer
    permission_classes=[AllowAny]


