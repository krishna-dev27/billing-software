from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=250)
    product_code=models.CharField(max_length=50,unique=True)
    product_description=models.TextField(blank=True)
    product_price=models.DecimalField(max_digits=10,decimal_places=2)
    gst_percent=models.IntegerField()
    stock_quantity=models.IntegerField()
    product_image=models.ImageField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name



    def get_absolute_url(self):
        return reverse('ProductDetail',kwargs={'pk':self.pk})
     

class Customer(models.Model):
    customer_name=models.CharField(max_length=200)
    customer_phone=models.CharField(max_length=22,unique=True)
    customer_email=models.EmailField(null=True,blank=True)
    customer_address=models.TextField()
    customer_gst_number=models.CharField(max_length=50, blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name
    
    def get_absolute_url(self):
        return reverse('CustomerDetail',kwargs={'pk':self.pk})



class Invoice(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    total_amount=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    gst_amount=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    grand_total=models.DecimalField(max_digits=10,decimal_places=2,default=0)

    def __str__(self):
        return f'Invoice {self.id} - {self.customer.customer_name}'
    

    




class InvoiceItem(models.Model):

    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.IntegerField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.product_name} - {self.quantity}"