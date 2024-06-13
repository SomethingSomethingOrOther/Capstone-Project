from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):

    def setUp(self):
        # Create test instances of Menu model
        self.menu1 = Menu.objects.create(title='Menu Item 1', price=10.99, inventory=50)
        self.menu2 = Menu.objects.create(title='Menu Item 2', price=15.50, inventory=30)

    def test_getall(self):
        
        client = APIClient()
        url = '/restaurant/menu/'  

        
        response = client.get(url)

        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)


        self.assertEqual(response.data, serializer.data)
