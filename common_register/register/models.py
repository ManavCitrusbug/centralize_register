from datetime import datetime,timezone
from turtle import mode

from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import (
    BaseUserManager
)


class UserManager(BaseUserManager):
    def create_user(self, email,first_name,last_name,username,password=None,password2=None):
        
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username,first_name,last_name,  password=None):
       
        """
        Creates and saves a superuser with the given email, first_name,last_name and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.create_user(
            email,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

        
class User(AbstractUser):
    email = models.EmailField(null=True, blank=True, unique=True)
    username = models.CharField(max_length=40, blank=True, null=True,unique=True)

    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    created_at = models.DateTimeField(default=datetime.now(tz=timezone.utc))
    updated_at = models.DateTimeField(default=datetime.now(tz=timezone.utc))
    is_admin=models.BooleanField(default=False)
    ref=models.CharField(max_length=40, blank=True, null=True,unique=True)
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username",'first_name','last_name']

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
    def __str__(self):
        return self.email
        
   