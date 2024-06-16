from django.db import models
from django.contrib.auth import authenticate
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.utils.translation import gettext as _


class MemberManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, password=None, **extra_fields):
        if not username:
            raise ValueError("The Email field must be set")
        user = self.model(
            username = username,
            first_name = first_name,
            last_name = last_name,
        )   
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, password=None, **extra_fields):
        user = self.create_user(
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return self.create_user(username, first_name, last_name, password, **extra_fields)
        # extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_superuser', True)
        # return self.create_user(email, password, **extra_fields)


class Member(AbstractBaseUser):
    username = models.CharField(_("نام کاربری یا ایمیل"), max_length=255, unique=True, primary_key=True) # either user or email
    first_name = models.CharField(_("نام") ,max_length=255)
    last_name = models.CharField(_("نام خانوادگی"),max_length=255)
    phone_number = models.CharField(_("شماره همراه"),max_length=12, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    last_login = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    has_module_perms = User.has_module_perms
    user_permissions = User.user_permissions

    
    objects = MemberManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']

    def __str__(self):
        return self.first_name
    def has_perm(self, user_, obj=None):
        return self.is_admin
