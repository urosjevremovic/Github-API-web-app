from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to='media/users/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.username