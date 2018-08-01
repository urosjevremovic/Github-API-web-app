from rest_framework.viewsets import ModelViewSet

from repository.models import Repository
from repository.serializers import RepositorySerializer


class RepositoryViewSet(ModelViewSet):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer