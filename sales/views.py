# sales/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Sale
from .forms import SaleForm

class SalesListView(ListView):
    model = Sale
    template_name = "sales/sale_list.html"
    context_object_name = "sales"
    paginate_by = 25
    queryset = Sale.objects.select_related('car', 'customer').order_by('-sale_date')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = SaleForm()   # form used in the modal for creating new sale
        return ctx

class SalesDetailView(DetailView):
    model = Sale
    template_name = "sales/sale_detail.html"
    context_object_name = "sale"

class SalesCreateView(CreateView):
    model = Sale
    form_class = SaleForm
    template_name = "sales/form.html"
    success_url = reverse_lazy('sales:sale-list')

class SalesUpdateView(UpdateView):
    model = Sale
    form_class = SaleForm
    template_name = "sales/form.html"
    success_url = reverse_lazy('sales:sale-list')

class SalesDeleteView(DeleteView):
    model = Sale
    template_name = "sales/confirm_delete.html"
    success_url = reverse_lazy('sales:sale-list')
