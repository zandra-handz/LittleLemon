from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):

    def test_get_item(self) -> None:
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        item = str(item)
        self.assertEqual(item, "IceCream : 80")


    