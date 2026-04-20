from django.contrib import admin

# Register your models here.
from .models import Inventory,StockMovement,Product,Address,Category

admin.site.register(Inventory)
admin.site.register(StockMovement)
admin.site.register(Product)
admin.site.register(Address)
admin.site.register(Category)
