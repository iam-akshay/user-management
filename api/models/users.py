from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.is_staff = kwargs.get("is_staff", False)
        user.is_admin = kwargs.get("is_admin", False)
        user.save(using=self._db)
        return user

    def create_staffuser(self, **kwargs):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(**kwargs)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(
        default=False
    )  # a admin user; non super-user
    is_admin = models.BooleanField(default=False)  # a superuser

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
