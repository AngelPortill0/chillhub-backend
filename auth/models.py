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
        ordering = ["last_login"]

    @classmethod
    def normalize_name(cls, name, change_to_lower=False) -> str:
        """
        Normalize the name by unicode form NFKC and lowercasing it

        Args:
            name (str): the name to be normalized

        Returns:
            str: the name normalized by unicode form NFKC and lowercase
        """
        return (
            unicodedata.normalize("NFKC", name).lower()
            if change_to_lower
            else unicodedata.normalize("NFKC", name)
        )

    @classmethod
    def normalize_email_domain(cls, email) -> str:
        """
        Normalize the email by lowercasing domain name

        Args:
            email (str): the email to be normalized

        Returns:
            str: the email normalized or empty string
        """
        unormalized_email = email
        normalized_email = ""

        if "@" in unormalized_email:
            email_name, domain_name = unormalized_email.strip.rstrip("@")
            normalized_email = f"{email_name}@{domain_name.lower()}"

        return normalized_email
