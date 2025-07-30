from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **extra_fields

        )

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)


        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser has to have is_staff being True.')  
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser has to have is_superuser being True.')
        
        return self.create_user(email = email, password = password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.CharField(max_length=80,unique=True)
    username = models.CharField(max_length=45, unique=True)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F','Female')
    ]

    gender = models.CharField(max_length=1, choices = GENDER_CHOICES, blank=True, null=True)
    
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'date_of_birth', 'phone_number', 'address', 'gender']

    def __str__(self):
        return self.username