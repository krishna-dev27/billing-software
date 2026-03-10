"""
URL configuration for billing_software project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from inventory.views import *
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ProductCreate/',ProductCreate.as_view(),name='ProductCreate'),
    path('ProductList/',ProductList.as_view(),name='ProductList'),

    path('ProductDetail/<int:pk>',ProductDetail.as_view(),name='ProductDetail'),
    path('Update/<int:pk>',ProductUpdate.as_view(),name='ProductUpdate'),
    path('ProductDelete/<int:pk>',ProductDelete.as_view(),name='ProductDelete'),


    path('CreateCustomer/',CreateCustomer.as_view(),name='CreateCustomer'),
    path('CustomerDetail/<int:pk>',CustomerDetail.as_view(),name='CustomerDetail'),
    path('CustomerUpdate/<int:pk>',CustomerUpdate.as_view(),name='CustomerUpdate'),
    path('CustomerList/',CustomerList.as_view(),name='CustomerList'),
    path('CustomerDelete/<int:pk>',CustomerDelete.as_view(),name='CustomerDelete'),



    path('InvoiceCreate/',InvoiceCreate.as_view(),name='InvoiceCreate'),
    path('InvoiceList/',InvoiceList.as_view(),name='InvoiceList'),
    path('add_invoice_item/<int:pk>',add_invoice_item,name='add_invoice_item'),
    


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
