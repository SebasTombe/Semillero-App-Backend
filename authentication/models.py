from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class AdminUserManager(BaseUserManager):
    def create_user(self, document_number, email, password=None, **extra_fields):
        if not document_number:
            raise ValueError('El campo Número de Documento debe estar establecido')
        if not email:
            raise ValueError('El campo Correo Electrónico debe estar establecido')
        
        email = self.normalize_email(email)
        user = self.model(document_number=document_number, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, document_number, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(document_number, email, password, **extra_fields)

class AdminUser(AbstractUser):
    email = models.EmailField(max_length=150, unique=True, default='x@x')
    document_number = models.CharField(max_length=20, unique=True, default='1111')  
    username = None  # Eliminar el campo username

    USERNAME_FIELD = 'document_number'
    REQUIRED_FIELDS = ['email']

    objects = AdminUserManager()  # Asignar el UserManager personalizado

    def __str__(self):
        return self.document_number