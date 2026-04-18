from django.contrib import admin

# Register your models here.
from .models import Inventory,StockMovement,Product

admin.site.register(Inventory)
admin.site.register(StockMovement)
admin.site.register(Product)
