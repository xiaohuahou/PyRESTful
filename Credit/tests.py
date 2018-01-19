import datetime
from Credit.views import CreditViewSet
from Credit.models import Credit
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate

# Create your tests here.
class CreditTests(APITestCase):

    @classmethod
    def setUpClass(cls):
        cls.admin = User.objects.create_user(username="credit_admin", email="test@test.com", password="test", is_superuser=True)
        super(CreditTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.admin.delete()
        super(CreditTests, cls).tearDownClass()

    def test_create_a_credit(self):
        factory = APIRequestFactory()
        request = factory.post('/v1/Credit/', {'appId': 1,'userId': 'user1'}, format='json')
        view = CreditViewSet.as_view(actions={'post':'create', 'get':'retrieve'})
        force_authenticate(request, user=CreditTests.admin)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Credit.objects.get(userId='user1'))
        self.assertEqual(Credit.objects.get(userId='user1').credit, 0)

    #
    def test_delete_a_credit(self):
        factory = APIRequestFactory()
        request = factory.post('/v1/Credit/', {'appId': 2, 'userId': 'user3', 'credit': 10}, format='json')
        view = CreditViewSet.as_view(actions={'post': 'create', 'get': 'retrieve', 'delete': 'destroy'})
        force_authenticate(request, user=CreditTests.admin)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Credit.objects.get(userId='user3').credit, 10)
        #delete request
        del_id = response.data['id']
        request = factory.delete('/v1/Credit/', format='json')
        force_authenticate(request, user=CreditTests.admin)
        response = view(request,  pk=del_id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Credit.objects.exists())
    #
    def test_increase_credit(self):
        factory = APIRequestFactory()
        request = factory.post('/v1/Credit/', {'appId': 1, 'userId': 'user1'}, format='json')
        view = CreditViewSet.as_view(actions={'post': 'create', 'get': 'retrieve'})
        force_authenticate(request, user=CreditTests.admin)
        response = view(request)
        self.assertEqual(Credit.objects.get(userId='user1').credit, 0)
        del_id = response.data['id']

        request = factory.patch('/v1/CheckIn/', {'credit' : 25},format='json')
        view = CreditViewSet.as_view(actions={'post': 'create', 'get': 'retrieve', 'patch':'partial_update', 'put' :'update'})
        force_authenticate(request, user=CreditTests.admin)
        response = view(request, pk=del_id)
        print(response)
        self.assertEqual(Credit.objects.get(userId='user1').credit, 25)

    def test_get_multipule_credit(self):
        factory = APIRequestFactory()
        request = factory.post('/v1/Credit/', {'appId': 1, 'userId': 'user1'}, format='json')
        view = CreditViewSet.as_view(actions={'post': 'create', 'get': 'retrieve'})
        force_authenticate(request, user=CreditTests.admin)
        view(request)

        request = factory.post('/v1/Credit/', {'appId': 1, 'userId': 'user2'}, format='json')
        view = CreditViewSet.as_view(actions={'post': 'create', 'get': 'retrieve'})
        force_authenticate(request, user=CreditTests.admin)
        view(request)

        request = factory.post('/v1/Credit/', {'appId': 2, 'userId': 'user2'}, format='json')
        view = CreditViewSet.as_view(actions={'post': 'create', 'get': 'retrieve'})
        force_authenticate(request, user=CreditTests.admin)
        view(request)

        #compose a get request
        request = factory.get('/v1/Credit/?appId=1', format='json')
        view = CreditViewSet.as_view(actions={'post': 'create', 'get': 'list'})
        force_authenticate(request, user=CreditTests.admin)
        response = view(request)
        self.assertEqual(len(response.data), 2)

        request = factory.get('/v1/Credit/?userId=user2', format='json')
        view = CreditViewSet.as_view(actions={'post': 'create', 'get': 'list'})
        force_authenticate(request, user=CreditTests.admin)
        response = view(request)
        self.assertEqual(len(response.data), 2)

        request = factory.get('/v1/Credit/', format='json')
        view = CreditViewSet.as_view(actions={'post': 'create', 'get': 'list'})
        force_authenticate(request, user=CreditTests.admin)
        response = view(request)
        self.assertEqual(len(response.data), 3)
