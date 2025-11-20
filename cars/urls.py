from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarListView.as_view(), name='car-list'),
    path('add/', views.CarCreateView.as_view(), name='car-add'),
    path('<int:pk>/', views.CarDetailView.as_view(), name='car-detail'),
    path('<int:pk>/edit/', views.CarUpdateView.as_view(), name='car-edit'),
    path('<int:pk>/delete/', views.CarDeleteView.as_view(), name='car-delete'),
]