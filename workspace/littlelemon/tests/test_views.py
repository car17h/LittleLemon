from restaurant.models import Menu
from django.test import TestCase

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100),
        Menu.objects.create(title="Pasta", price=90, inventory=110)

    def test_getall(self):
       item1 = Menu.objects.all()
       self.assertEqual(str(item1[1]), "Pasta : 90.00")



