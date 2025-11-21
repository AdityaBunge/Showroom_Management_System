from django.urls import path
from . import views

urlpatterns = [
    path('sales/', views.SalesListView.as_view(), name='sales-list'),
    path('sales/<int:pk>/', views.SalesDetailView.as_view(), name='sales-detail'),
    path('sales/create/', views.SalesCreateView.as_view(), name='sales-create'),
    path('sales/<int:pk>/update/', views.SalesUpdateView.as_view(), name='sales-update'),
    path('sales/<int:pk>/delete/', views.SalesDeleteView.as_view(), name='sales-delete'),
]