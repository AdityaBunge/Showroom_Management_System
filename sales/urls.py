from django.urls import path
from . import views

app_name = "sales"

urlpatterns = [
    path('', views.SalesListView.as_view(), name='sales-list'),
    path('<int:pk>/', views.SalesDetailView.as_view(), name='sales-detail'),
    path('create/', views.SalesCreateView.as_view(), name='sales-create'),
    path('<int:pk>/update/', views.SalesUpdateView.as_view(), name='sales-update'),
    path('<int:pk>/delete/', views.SalesDeleteView.as_view(), name='sales-delete'),
]