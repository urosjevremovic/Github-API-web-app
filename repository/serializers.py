from rest_framework import serializers

from repository.models import Repository


class RepositorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Repository
        fields = '__all__'
