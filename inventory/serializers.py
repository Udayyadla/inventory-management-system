from rest_framework import serializers
from .models import Product, Supplier, Category, Warehouse, Inventory, StockMovement


READ_ONLY_FIELDS = ("id", "created_at", "updated_at")

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = READ_ONLY_FIELDS

    def create(self,validated_data):
        if isinstance(validated_data,list):
            return Product.objects.bulk_create([Product(**item) for item in validated_data])
        return super().create(validated_data)

        

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
        read_only_fields = READ_ONLY_FIELDS

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = READ_ONLY_FIELDS

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'
        read_only_fields = READ_ONLY_FIELDS

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'
        read_only_fields = READ_ONLY_FIELDS
class StockMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockMovement
        fields = '__all__'
        read_only_fields = READ_ONLY_FIELDS

    