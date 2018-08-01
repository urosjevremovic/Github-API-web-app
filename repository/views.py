from rest_framework.viewsets import ModelViewSet

from repository.models import Repository
from repository.permissions import IsRepositoryOwnerOrAdminUserOrReadOnly
from repository.serializers import RepositorySerializer


class RepositoryViewSet(ModelViewSet):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
    permission_classes = [IsRepositoryOwnerOrAdminUserOrReadOnly, ]