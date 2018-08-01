from django.conf import settings
from django.db import models


class Repository(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    description = models.TextField()
    url = models.URLField()
    language = models.CharField(max_length=32)
    watchers_count = models.PositiveIntegerField()

    def __str__(self):
        return self.name