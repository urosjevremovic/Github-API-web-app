from rest_framework.viewsets import ModelViewSet

from user.models import User
from user.permissions import IsAccountwnerOrAdminUserOrReadOnly
from user.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAccountwnerOrAdminUserOrReadOnly, ]
    lookup_field = 'username'
