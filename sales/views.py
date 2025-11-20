from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Sale
from django.forms import modelform_factory

SaleForm = modelform_factory(Sale, fields='__all__')

class SalesListView(ListView):
    model = Sale
    template_name = "sales/list.html"
    context_object_name = "sales"
    paginate_by = 25

class SalesDetailView(DetailView):
    model = Sale
    template_name = "sales/detail.html"
    context_object_name = "sale"

class SalesCreateView(CreateView):
    model = Sale
    form_class = SaleForm
    template_name = "sales/form.html"
    success_url = reverse_lazy('sales:sales-list')

class SalesUpdateView(UpdateView):
    model = Sale
    form_class = SaleForm
    template_name = "sales/form.html"
    success_url = reverse_lazy('sales:sales-list')

class SalesDeleteView(DeleteView):
    model = Sale
    template_name = "sales/confirm_delete.html"
    success_url = reverse_lazy('sales:sales-list')

# optional function-based fallback
def sales_list(request):
    sales = Sale.objects.select_related('car', 'customer').all()
    return render(request, 'sales/list.html', {'sales': sales})