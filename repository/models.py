from django.db import models

from user.models import GitUser


class Repository(models.Model):

    owner = models.ForeignKey(GitUser, on_delete=models.CASCADE, related_name='repositories')
    name = models.CharField(max_length=32)
    description = models.TextField(null=True, blank=True)
    url = models.URLField()
    language = models.CharField(max_length=32, blank=True, null=True)
    watchers_count = models.PositiveIntegerField()

    def __str__(self):
        return self.name