from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password,password_2, **extra_fields):
        if not email:
            raise ValueError('O campo de e-mail deve ser preenchido')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.set_password_2(password_2)
        user.save(using=self._db)
        return user
    
def create_superuser(self, email, first_name, last_name, password, password_2, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        return self.create_user(email, first_name, last_name, password, password_2, **extra_fields)

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'address', 'email']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
