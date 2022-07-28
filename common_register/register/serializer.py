
from rest_framework import serializers
from register.models import *
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import requests
import json





class Registerserializer(serializers.ModelSerializer):
   class Meta:
       model = User

       fields = ['id', 'username', 'first_name',
           'last_name', 'email', 'password','ref']

   def validate(self, data):
      username = data.get('username')
      first_name = data.get('first_name')
      last_name = data.get('last_name')
      email = data.get('email')
      password = data.get('password')
      if username == '':
          raise serializers.ValidationError('Enter the Username')
      if first_name == '':
         raise serializers.ValidationError('Enter the firstname')
      if last_name == '':
         raise serializers.ValidationError('Enter the last name')
      if email == '':
         raise serializers.ValidationError('Enter the email')
      if password == '':
         raise serializers.ValidationError('Enter the password')
      return data
   
   def create(self, validated_data):
      password=validated_data.pop('password')
      validated_data["password"] = make_password(password)
      instance = super().create(validated_data)
      url = "http://127.0.0.1:5532/userregister/"

      payload = json.dumps({
            "username": instance.username,
            "first_name": instance.first_name,
            "last_name": instance.last_name,
            "email": instance.email,
            "password": password
            })
      headers = {
      'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      # print(response.json(),'******')
      instance.ref=response.json()['ref']
      instance.save()
      # print(response.text)
      return instance
