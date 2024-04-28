from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(unique=True, max_length=25)
    email = models.EmailField(blank=False, unique=True)
    password = models.CharField(max_length=200)
    is_email_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login_at = models.DateTimeField(default=None, null=True)

    # Override fields from abstract user
    last_login = None
    date_joined = None

    class Meta:
        db_table = "user"
        ordering = ["-last_login_at"]
