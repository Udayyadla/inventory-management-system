from django.db import models
import uuid

# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Product(BaseModel):
    name = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null= False)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=False)
    supplier = models.ForeignKey("Supplier", on_delete=models.PROTECT, null=False)
    sku = models.CharField(max_length=50,null=False, unique=True)
    reorder_level = models.PositiveIntegerField(default=10,null=False)

class Supplier(BaseModel):
    name = models.CharField(max_length=255, null=False)
    address = models.ForeignKey("Address", on_delete=models.PROTECT, null=False)
    phone = models.CharField(max_length=20, null=True,blank=True)
    email = models.EmailField(blank=True,null=True)

class Category(BaseModel):
    name = models.CharField(max_length=255, null=False)

class Warehouse(BaseModel):
    name = models.CharField(max_length=255, null=False)
    address = models.ForeignKey("Address", on_delete=models.PROTECT, null=False)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(blank=True,null=True)

class Address(BaseModel):
    lane1 = models.TextField(null=False)
    lane2 = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=255, null=False)
    state = models.CharField(max_length=255, null=False)
    country = models.CharField(max_length=255, null=False)
    pincode = models.CharField(max_length=10, null=False)

class StockMovement(BaseModel):
    movement_type_choices = (
        ("IN", "IN"),
        ("OUT","OUT"),
        ("ADJUSTMENT", "ADJUSTMENT"),
        ("TRANSFER_IN", "TRANSFER_IN"),
        ("TRANSFER_OUT", "TRANSFER_OUT"),)
    product = models.ForeignKey("Product", on_delete=models.PROTECT, null=False)
    warehouse = models.ForeignKey("Warehouse", on_delete=models.PROTECT, null=False)
    movement_type = models.CharField(max_length=50, choices=movement_type_choices,null=False)
    quantity = models.PositiveIntegerField(null=False)
    notes = models.TextField(null=True, blank=True)

class Inventory(BaseModel):
    product = models.ForeignKey("Product", on_delete=models.PROTECT, null=False)
    warehouse = models.ForeignKey("Warehouse", on_delete=models.PROTECT, null=False)
    stock = models.PositiveIntegerField(default=0)
    is_low_stock = models.BooleanField(default=False)

    class Meta:
        unique_together = ("product", "warehouse")
    

