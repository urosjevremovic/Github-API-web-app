from django.db import models


class GitUser(models.Model):
    username = models.CharField(max_length=32)
    avatar = models.ImageField(upload_to='media/users/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.username
