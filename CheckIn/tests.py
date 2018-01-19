import datetime
from CheckIn.views import CheckInViewSet
from CheckIn.models import CheckIn
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate

# Create your tests here.
class CheckInTests(APITestCase):

    @classmethod
    def setUpClass(cls):
        cls.admin = User.objects.create_user(username="checkin_admin", email="test@test.com", password="test", is_superuser=True)
        super(CheckInTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.admin.delete()
        super(CheckInTests, cls).tearDownClass()

    def test_create_a_checkin(self):
        factory = APIRequestFactory()
        request = factory.post('/v1/CheckIn/', {'appId': 1,'userId': 'user1'}, format='json')
        view = CheckInViewSet.as_view(actions={'post':'create', 'get':'retrieve'})
        force_authenticate(request, user=CheckInTests.admin)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(CheckIn.objects.get(userId='user1'))
        self.assertEqual(CheckIn.objects.get(userId='user1').datetime.date(), datetime.date.today())

    def test_create_a_pre_checkin(self):
        factory = APIRequestFactory()
        request = factory.post('/v1/CheckIn/', {'appId': 2, 'userId': 'user2', 'datetime':'2018-01-01T01:01:01'}, format='json')
        view = CheckInViewSet.as_view(actions={'post': 'create', 'get': 'retrieve'})
        force_authenticate(request, user=CheckInTests.admin)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(CheckIn.objects.get(userId='user2'))
        self.assertEqual(CheckIn.objects.get(userId='user2').datetime.date(), datetime.date(2018,1,1))

    def test_delete_a_checkin(self):
        factory = APIRequestFactory()
        request = factory.post('/v1/CheckIn/', {'appId': 2, 'userId': 'user3', 'datetime': '2018-01-01T01:01:01'}, format='json')
        view = CheckInViewSet.as_view(actions={'post': 'create', 'get': 'retrieve', 'delete': 'destroy'})
        force_authenticate(request, user=CheckInTests.admin)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #delete request
        del_id = response.data['id']
        request = factory.delete('/v1/CheckIn/', format='json')
        force_authenticate(request, user=CheckInTests.admin)
        response = view(request,  pk=del_id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(CheckIn.objects.exists())

    def test_get_multipule_checkin(self):
        factory = APIRequestFactory()
        request = factory.post('/v1/CheckIn/', {'appId': 1, 'userId': 'user1'}, format='json')
        view = CheckInViewSet.as_view(actions={'post': 'create', 'get': 'retrieve'})
        force_authenticate(request, user=CheckInTests.admin)
        view(request)

        request = factory.post('/v1/CheckIn/', {'appId': 1, 'userId': 'user2'}, format='json')
        view = CheckInViewSet.as_view(actions={'post': 'create', 'get': 'retrieve'})
        force_authenticate(request, user=CheckInTests.admin)
        view(request)

        request = factory.post('/v1/CheckIn/', {'appId': 2, 'userId': 'user2'}, format='json')
        view = CheckInViewSet.as_view(actions={'post': 'create', 'get': 'retrieve'})
        force_authenticate(request, user=CheckInTests.admin)
        view(request)

        #compose a get request
        request = factory.get('/v1/CheckIn/?appId=1', format='json')
        view = CheckInViewSet.as_view(actions={'post': 'create', 'get': 'list'})
        force_authenticate(request, user=CheckInTests.admin)
        response = view(request)
        self.assertEqual(len(response.data), 2)

        request = factory.get('/v1/CheckIn/?userId=user2', format='json')
        view = CheckInViewSet.as_view(actions={'post': 'create', 'get': 'list'})
        force_authenticate(request, user=CheckInTests.admin)
        response = view(request)
        self.assertEqual(len(response.data), 2)

        request = factory.get('/v1/CheckIn/', format='json')
        view = CheckInViewSet.as_view(actions={'post': 'create', 'get': 'list'})
        force_authenticate(request, user=CheckInTests.admin)
        response = view(request)
        self.assertEqual(len(response.data), 3)