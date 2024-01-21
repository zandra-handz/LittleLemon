from django.test import TestCase, Client
from django.contrib.auth.models import User
from restaurant.views import Menu
from django.urls import reverse
from rest_framework import status
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.blt = Menu.objects.create(title='BLT', price=7.00, inventory=10)
        self.tacopizza = Menu.objects.create(title='Taco Pizza', price=10.00, inventory=7)
        self.margpizza = Menu.objects.create(title='Margherita Pizza', price=9.00, inventory=5)
    
    def login_as_testuser(self):
        self.client.login(username='testuser', password='testpassword')
    
    def test_view_auth(self):
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_getall(self):
        self.loginAsTestUser()
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)
