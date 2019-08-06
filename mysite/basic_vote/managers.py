from django.contrib.auth.base_user import BaseUserManager
import hashlib


class CustomUserManager(BaseUserManager):

    def create_user(self, username, **extra_fields):

        username = hash_username(username)
        user = self.model(username=username, **extra_fields)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        username = 'admin'
        user = self.model(username=username, **extra_fields)
        user.is_admin = True
        user.is_staff = True
        user.set_password(password)
        user.save()
        return user


def hash_username(username):
    return hashlib.md5(username.encode('utf-8')).hexdigest()
