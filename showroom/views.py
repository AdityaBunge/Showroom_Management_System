from django.shortcuts import render
from datetime import datetime
from cars.models import Car
from customers.models import Customer
from sales.models import Sale

def index(request):
    # Get statistics for dashboard
    total_cars = Car.objects.count()
    total_customers = Customer.objects.count()
    total_sales = Sale.objects.count()
    
    # Calculate total revenue
    total_revenue = sum(sale.sale_price for sale in Sale.objects.all())
    
    # Recent sales (last 5)
    recent_sales = Sale.objects.select_related('car', 'customer').order_by('-sale_date')[:5]
    
    # Recent cars (last 5)
    recent_cars = Car.objects.order_by('-created_at')[:5]
    
    context = {
        'current_year': datetime.now().year,
        'total_cars': total_cars,
        'total_customers': total_customers,
        'total_sales': total_sales,
        'total_revenue': total_revenue,
        'recent_sales': recent_sales,
        'recent_cars': recent_cars,
    }
    return render(request, 'dashboard.html', context)
