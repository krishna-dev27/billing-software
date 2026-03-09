from django.shortcuts import render
from inventory.models import *
from inventory.forms import *
from django.http import HttpResponse
# Create your views here.



from django.views.generic import CreateView,ListView,DeleteView,DetailView,UpdateView
from django.urls import reverse_lazy


class ProductCreate(CreateView):
    model=Product
    fields='__all__'
    success_url=reverse_lazy('ProductList')


class ProductList(ListView):
    model=Product
    context_object_name='products'


class ProductDetail(DetailView):
    model=Product
    context_object_name='po'



class ProductUpdate(UpdateView):
    model=Product
    fields='__all__'


class ProductDelete(DeleteView):
    model=Product
    context_object_name='PO'
    success_url=reverse_lazy('ProductList')



# CUSTOMER SECTION


class CreateCustomer(CreateView):
    model=Customer
    fields='__all__'



class CustomerDetail(DetailView):
    model=Customer
    context_object_name='CO'

class CustomerUpdate(UpdateView):
    model=Customer
    fields='__all__'


class CustomerList(ListView):
    model=Customer
    context_object_name='customerobjects'


class CustomerDelete(DeleteView):
    model=Customer
    context_object_name='CO'
    success_url=reverse_lazy('CustomerList')


