from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelform_factory
from .models import Inventory

InventoryForm = modelform_factory(Inventory, fields='__all__')

def inventory_list(request):
    items = Inventory.objects.all()
    return render(request, 'inventory/list.html', {'items': items})

def inventory_detail(request, item_id):
    item = get_object_or_404(Inventory, pk=item_id)
    return render(request, 'inventory/detail.html', {'item': item})

def add_inventory_item(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryForm()
    return render(request, 'inventory/form.html', {'form': form})

def edit_inventory_item(request, item_id):
    item = get_object_or_404(Inventory, pk=item_id)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryForm(instance=item)
    return render(request, 'inventory/form.html', {'form': form, 'item': item})

def delete_inventory_item(request, item_id):
    item = get_object_or_404(Inventory, pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('inventory_list')
    return render(request, 'inventory/confirm_delete.html', {'item': item})