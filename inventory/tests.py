from django.test import TestCase
from .models import InventoryItem

class InventoryItemModelTest(TestCase):

    def setUp(self):
        InventoryItem.objects.create(name="Test Car", quantity=10, price=20000)

    def test_inventory_item_creation(self):
        item = InventoryItem.objects.get(name="Test Car")
        self.assertEqual(item.quantity, 10)
        self.assertEqual(item.price, 20000)

    def test_inventory_item_str(self):
        item = InventoryItem.objects.get(name="Test Car")
        self.assertEqual(str(item), "Test Car")