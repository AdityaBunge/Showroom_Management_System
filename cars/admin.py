from django.contrib import admin
from .models import Car

admin.site.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'make', 'model', 'year', 'price')
    search_fields = ('make', 'model', 'year')