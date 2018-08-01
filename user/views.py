from rest_framework.viewsets import ModelViewSet

from repository.models import Repository
from user.models import GitUser
from user.serializers import GitUserSerializer
from user.service import user_data_by_username


class GitUserViewSet(ModelViewSet):
    queryset = GitUser.objects.all()
    serializer_class = GitUserSerializer
    lookup_field = 'username'

    def retrieve(self, request, *args, **kwargs):
        self.kwargs['username'] = self.kwargs['username'].title()
        exists = GitUser.objects.filter(username=self.kwargs['username'])
        if not exists:
            user_data = user_data_by_username(self.kwargs['username'])
            if user_data:
                user = GitUser.objects.create(username=user_data[0]['username'].title(), avatar=user_data[0]['avatar'],)
                for repo in user_data[1]:
                    repository = Repository.objects.create(owner=user, name=repo['name'], language=repo['language'],
                                                           url=repo['url'], watchers_count=repo['watchers_count'],
                                                           description=repo['description'])
                    repository.save()
                user.save()
            else:
                pass
        return super().retrieve(request, *args, **kwargs)