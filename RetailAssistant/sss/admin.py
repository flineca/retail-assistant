from django.contrib import admin

# Register your models here.

from .models import Product, Customer, Supplier, Technician, SaleHistory, StockHistory, ServiceHistory

admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(Technician)
admin.site.register(SaleHistory)
admin.site.register(StockHistory)
admin.site.register(ServiceHistory)