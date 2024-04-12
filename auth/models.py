import unicodedata
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


class User(AbstractBaseUser):
    username_validator = UnicodeUsernameValidator()

    uuid = models.UUIDField(primary_key=True)
    username = models.CharField(
        unique=True,
        max_length=20,
        validators=[username_validator],
        error_messages="That Username already exists",
    )
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True, error_messages="That Email already exists")
    is_active = models.BooleanField(
        default=True, db_comment="Soft delete existing user when False"
    )
    is_email_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(null=True)

    class Meta:
        db_table = "user"
        verbose_name = "user"
        verbose_name_plural = "users"

    @classmethod
    def normalize_username(cls, username) -> str:
        """
        Normalize the username by unicode form NFKC and lowercasing it

        Args:
            username (str): the username to be normalized

        Returns:
            str: the username normalized by unicode form NFKC and lowercase
        """
        return unicodedata.normalize("NFKC", username).lower()
