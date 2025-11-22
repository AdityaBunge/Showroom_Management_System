# inventory/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Inventory
from .forms import InventoryForm
from django.db.models import F, Q

class InventoryListView(ListView):
    model = Inventory
    template_name = "inventory/inventory_list.html"
    context_object_name = "items"
    paginate_by = 20

    def get_queryset(self):
        qs = super().get_queryset().select_related('car')
        # optional filtering by ?q=search
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(Q(car__make__icontains=q) | Q(car__model__icontains=q) | Q(location__icontains=q))
        return qs

class InventoryDetailView(DetailView):
    model = Inventory
    template_name = "inventory/inventory_detail.html"
    context_object_name = "item"

class InventoryCreateView(CreateView):
    model = Inventory
    form_class = InventoryForm
    template_name = "inventory/form.html"
    success_url = reverse_lazy('inventory:inventory-list')

class InventoryUpdateView(UpdateView):
    model = Inventory
    form_class = InventoryForm
    template_name = "inventory/form.html"
    success_url = reverse_lazy('inventory:inventory-list')

class InventoryDeleteView(DeleteView):
    model = Inventory
    template_name = "inventory/confirm_delete.html"
    success_url = reverse_lazy('inventory:inventory-list')
