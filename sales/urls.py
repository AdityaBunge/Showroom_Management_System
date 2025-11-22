# sales/urls.py
from django.urls import path
from . import views

app_name = "sales"

urlpatterns = [
    path('', views.SalesListView.as_view(), name='sale-list'),
    path('create/', views.SalesCreateView.as_view(), name='sale-create'),
    path('<int:pk>/', views.SalesDetailView.as_view(), name='sale-detail'),
    path('<int:pk>/update/', views.SalesUpdateView.as_view(), name='sale-update'),
    path('<int:pk>/delete/', views.SalesDeleteView.as_view(), name='sale-delete'),
]
