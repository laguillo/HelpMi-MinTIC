from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
from .choises import *

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length=15, unique=True)
    password = models.CharField('Password', max_length=256)
    rol = models.CharField('Rol', max_length=50, choices=rol, default='P')
    nombre = models.CharField('Nombre', max_length=30)
    apellido = models.CharField('Apellido', max_length=30)
    tipoDocumento = models.CharField('Tipo de documento', max_length=50, choices=tipoDoc, default='CC')
    documento = models.PositiveIntegerField('Documento', default=0)
    email = models.EmailField('Email', max_length=100)
    celular = models.CharField('Celular', max_length=10)
    direccion = models.CharField('Dirección', max_length=50)
    genero = models.CharField('Genero', max_length=50, choices=genero, default="F")
    
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'username'
