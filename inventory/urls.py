from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),
    path('add/', views.add_inventory_item, name='add_inventory_item'),
    path('<int:item_id>/', views.inventory_detail, name='inventory_detail'),
    path('<int:item_id>/edit/', views.edit_inventory_item, name='edit_inventory_item'),
    path('<int:item_id>/delete/', views.delete_inventory_item, name='delete_inventory_item'),
]