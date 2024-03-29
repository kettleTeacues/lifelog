from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# バリデーション用
from django.core.validators import MinLengthValidator, RegexValidator

import uuid, datetime

class myUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('emailを入力してください。')
        
        user = self.model(
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user

class customuser(AbstractBaseUser, PermissionsMixin):
    user_id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    email = models.EmailField(unique=True, null=False)
    created_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = myUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
    ]

    def __str__(self):
        return self.email

class userActivateTokenManager(models.Manager):
    def activateUser(self, activate_token):
        userActivateToken = self.filter(
            activate_token = activate_token,
        ).first()

        if hasattr(userActivateToken, 'user_id'):
            user = userActivateToken.user_id
            user.is_active = True
            user.save()
            return user

class userActivateToken(models.Model):
    token_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activate_token = models.UUIDField(default=uuid.uuid4)

    objects = userActivateTokenManager()

class sampleUser(models.Model):
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(blank=True, null=True, max_length=100)