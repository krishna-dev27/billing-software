from django.contrib import admin

# Register your models here.
from inventory.models import *
admin.site.register(Product)

admin.site.register(Customer)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)