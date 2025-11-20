from django.test import TestCase
from .models import Car

class CarModelTest(TestCase):

    def setUp(self):
        Car.objects.create(make="Toyota", model="Camry", year=2020, price=24000)
        Car.objects.create(make="Honda", model="Accord", year=2021, price=26000)

    def test_car_creation(self):
        car = Car.objects.get(make="Toyota")
        self.assertEqual(car.model, "Camry")
        self.assertEqual(car.year, 2020)
        self.assertEqual(car.price, 24000)

    def test_car_str(self):
        car = Car.objects.get(make="Honda")
        self.assertEqual(str(car), "Honda Accord (2021)")