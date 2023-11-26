from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Item1", price=10, inventory=50)
        Menu.objects.create(title="Item2", price=15, inventory=30)

    def test_getall(self):
        client = APIClient()
        response = client.get('http://localhost:8000/api/menu-items/') 
        self.assertEqual(response.status_code, 200)

        expected_data = [
            {"title": "Item1", "price": "10.00", "inventory": 50},
            {"title": "Item2", "price": "15.00", "inventory": 30},
        ]
        
        self.assertEqual(response.data, expected_data)