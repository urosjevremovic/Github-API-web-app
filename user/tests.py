from rest_framework import status
from rest_framework.test import APITestCase

from repository.models import Repository
from user.models import GitUser
from user.serializers import GitUserSerializer


class GetAllUsersTest(APITestCase):

    def setUp(self):
        self.gituser = GitUser.objects.create(username='Andrew', )
        Repository.objects.create(owner=self.gituser, name='My repo', language='Go',
                                  url='http://myurl.com', watchers_count=6,
                                  description='my description')

    def test_get_all_git_users(self):
        response = self.client.get('http://127.0.0.1:8000/gituser/')
        gitusers = GitUser.objects.all()
        serializer = GitUserSerializer(gitusers, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Andrew', str(response.data))


class GetSingleGitUserTest(APITestCase):

    def setUp(self):
        self.gituser = GitUser.objects.create(username='Andrew', )
        Repository.objects.create(owner=self.gituser, name='My repo', language='Go',
                                  url='http://myurl.com', watchers_count=6,
                                  description='my description')

    def test_get_valid_single_git_user(self):
        response = self.client.get(f'http://127.0.0.1:8000/gituser/Andrew/')
        gituser = GitUser.objects.get(pk=self.gituser.pk)
        serializer = GitUserSerializer(gituser)
        self.assertEqual(gituser.__str__(), 'Andrew')
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_git_user_returns_404(self):
        response = self.client.get('http://127.0.0.1:8000/gituser/NoneExistingUser/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_retrieves_single_git_user_data_from_external_API(self):
        response = self.client.get('http://127.0.0.1:8000/gituser/Neko/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateSingleGitUserTest(APITestCase):

    def setUp(self):
        self.payload = {
            'username': 'Andrew',
            'avatar': 'https://avatars2.githubusercontent.com/u/1060?s=460&v=4'
        }

    def test_create_with_valid_data_returns_403_when_not_logged_in(self):
        response = self.client.post('http://127.0.0.1:8000/gituser/', data=self.payload,
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
