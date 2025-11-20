from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Car

class CarListView(ListView):
    model = Car
    template_name = "cars/list.html"
    context_object_name = "cars"
    paginate_by = 20

class CarDetailView(DetailView):
    model = Car
    template_name = "cars/detail.html"
    context_object_name = "car"

class CarCreateView(CreateView):
    model = Car
    fields = '__all__'
    template_name = "cars/form.html"
    success_url = reverse_lazy('car-list')

class CarUpdateView(UpdateView):
    model = Car
    fields = '__all__'
    template_name = "cars/form.html"
    success_url = reverse_lazy('car-list')


class CarDeleteView(DeleteView):
    model = Car
    template_name = "cars/confirm_delete.html"
    success_url = reverse_lazy('car-list')

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/list.html', {'cars': cars})

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'cars/detail.html', {'car': car})