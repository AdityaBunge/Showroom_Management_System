from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', include('cars.urls')),
    path('customers/', include('customers.urls')),
    path('sales/', include('sales.urls')),
    path('inventory/', include('inventory.urls')),
    path('', views.index, name='index'),
]
