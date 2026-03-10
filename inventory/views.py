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





#Invoice code

class InvoiceCreate(CreateView):
    model=Invoice
    form_class=InvoiceForm
    template_name='inventory/create_invoice.html'
    success_url=reverse_lazy('InvoiceList')


class InvoiceList(ListView):
    model=Invoice
    context_object_name='invoices'


def add_invoice_item(request,pk):
    invoice=Invoice.objects.filter(pk=pk)[0]
    EIIMFO=InvoiceItemForm()

    if request.method=='POST':
        pass

    d={'EIIMFO':EIIMFO,'invoice':invoice}
    return render(request,'inventory/add_invoice_item.html',d)

   
