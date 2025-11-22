# inventory/models.py
from django.db import models
from cars.models import Car

class Inventory(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='inventory_items')
    quantity = models.PositiveIntegerField(default=0)
    min_stock = models.PositiveIntegerField(default=0, help_text="Alert if quantity <= min_stock")
    location = models.CharField(max_length=120, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        verbose_name_plural = "Inventory"

    def __str__(self):
        return f"{self.car} — {self.quantity}"
