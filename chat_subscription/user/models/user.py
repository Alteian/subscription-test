from django.db import models
from django.contrib.auth.base_user import BaseUserManager

from chat_subscription.shared.models.base_user import BaseUserModel


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, model=None, **extra_fields):
        if not model:
            model = self.model

        email = email.lower()
        if not email:
            raise ValueError("Users must have an email address")

        user = model(
            email=self.normalize_email(email),
        )
        [setattr(user, k, v) for k, v in extra_fields.items()]
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name):
        user = self.create_user(email, password=password, model=User)
        user.first_name = first_name
        user.last_name = last_name
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_email(self, email):
        return self.get_queryset().get(email=email.lower())

    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD + "__iexact": username})


class User(BaseUserModel):
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    objects = UserManager()

    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
