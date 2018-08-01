from rest_framework import serializers

from user.models import GitUser


class GitUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = GitUser
        fields = ['username', 'avatar']
        lookup_field = 'username'
