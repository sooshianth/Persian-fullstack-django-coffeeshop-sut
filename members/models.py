from django.db import models
from django.contrib.auth import authenticate
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext as _


class MemberManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, password=None, **extra_fields):
        if not username:
            raise ValueError("پر کردن بخش نام کاربری الزامی است")
        user = self.model(
            username = username,
            first_name = first_name,
            last_name = last_name,
        )   
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, first_name, last_name, password, **extra_fields)

class Member(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_("نام کاربری یا ایمیل"), max_length=255, unique=True, primary_key=True) # either user or email
    first_name = models.CharField(_("نام") ,max_length=255)
    last_name = models.CharField(_("نام خانوادگی"),max_length=255)
    phone_number = models.CharField(_("شماره همراه"),max_length=12, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    last_login = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    
    objects = MemberManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.first_name
