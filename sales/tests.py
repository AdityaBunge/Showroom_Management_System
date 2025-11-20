from django.test import TestCase
from .models import Sale

class SaleModelTest(TestCase):
    def setUp(self):
        self.sale = Sale.objects.create(
            car_id=1,
            customer_id=1,
            sale_price=20000,
            sale_date='2023-01-01'
        )

    def test_sale_creation(self):
        self.assertEqual(self.sale.car_id, 1)
        self.assertEqual(self.sale.customer_id, 1)
        self.assertEqual(self.sale.sale_price, 20000)
        self.assertEqual(str(self.sale.sale_date), '2023-01-01')

    def test_string_representation(self):
        self.assertEqual(str(self.sale), f'Sale of car {self.sale.car_id} to customer {self.sale.customer_id}')