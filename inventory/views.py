from django.shortcuts import render,redirect
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

'''class InvoiceCreate(CreateView):
    model=Invoice
    form_class=InvoiceForm
    template_name='inventory/create_invoice.html'
   


class InvoiceList(ListView):
    model=Invoice
    context_object_name='invoices'


def add_invoice_item(request,pk):
    invoice=Invoice.objects.filter(pk=pk)[0]
    EIIMFO=InvoiceItemForm()

    if request.method=='POST':
        pass

    d={'EIIMFO':EIIMFO,'invoice':invoice}
    return render(request,'inventory/add_invoice_item.html',d)'''

def InvoiceCreate(request):
    EIFO=InvoiceForm()
    d={'EIFO':EIFO}
    if request.method=='POST':
        IFO=InvoiceForm(request.POST)
        if IFO.is_valid():
            SO=IFO.save()
            return redirect('add_invoice_item',pk=SO.id)
        
        else:
            EIFO = InvoiceForm()
        d={'EIFO':EIFO}





    return render(request,'inventory/create_invoice.html',d)



def add_invoice_item(request,pk):
    IO=Invoice.objects.get(pk=pk)
    EIIMFO=InvoiceItemForm()
    BillObj=InvoiceItem.objects.filter(invoice=IO)
    
    d={'IO':IO,'EIIMFO':EIIMFO,'BillObj':BillObj}
    if request.method=='POST':
        IIMFO=InvoiceItemForm(request.POST)
        if IIMFO.is_valid():
            MIIMFO=IIMFO.save(commit=False)
            MIIMFO.invoice=IO
            MIIMFO.price= MIIMFO.product.product_price
            MIIMFO.total = MIIMFO.quantity * MIIMFO.price
            MIIMFO.save()
            




            
            
            return redirect(reverse('add_invoice_item', args=[pk]))
            

    return render(request,'inventory/add_invoice_item.html',d)

def delete_item(request, pk):
    item = InvoiceItem.objects.get(pk=pk)
    invoice_id = item.invoice.id   # get invoice id before delete
    item.delete()

    return redirect(reverse('add_invoice_item', args=[invoice_id]))

    
    

def dummy(request):
    return render(request,'inventory/dummy.html')



def home(request):
    return render(request,'inventory/home.html')