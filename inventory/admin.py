from django.contrib import admin

# Register your models here.
from .models import Inventory,StockMovement

admin.site.register(Inventory)
admin.site.register(StockMovement)
