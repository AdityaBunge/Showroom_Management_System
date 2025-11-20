
# customers/urls.py
from django.urls import path
from . import views

app_name = "customers"

urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    path('add/', views.customer_add, name='customer-add'),  # changed from 'customer_add' to 'customer-add'
    path('<int:pk>/', views.customer_detail, name='customer-detail'),  # optional
]