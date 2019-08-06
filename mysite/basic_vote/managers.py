from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
import hashlib


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, username, **extra_fields):
        """
        Create and save a User with the given email and password.
        """

        username = hash_username(username)
        user = self.model(username=username, **extra_fields)
        user.save()
        return user


def hash_username(username):
    return hashlib.md5(username.encode('utf-8')).hexdigest()
