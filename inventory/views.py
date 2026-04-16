from rest_framework import generics
from .models import Inventory, Product, StockMovement, Supplier, Category, Warehouse
from .serializers import (
    InventorySerializer,
    ProductSerializer,
    StockMovementSerializer,
    SupplierSerializer,
    CategorySerializer,
    WarehouseSerializer,
)

class BaseListCreateView(generics.ListCreateAPIView):
    pass

class BaseDetailView(generics.RetrieveUpdateDestroyAPIView):
    pass
# Create your views here.
class ProductList(BaseListCreateView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(BaseDetailView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class StockMovementList(BaseListCreateView):
    queryset = StockMovement.objects.all()
    serializer_class = StockMovementSerializer


class StockMovementDetail(BaseDetailView):
    queryset = StockMovement.objects.all()
    serializer_class = StockMovementSerializer


class InventoryList(BaseListCreateView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventoryDetail(BaseDetailView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class SupplierList(BaseListCreateView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierDetail(BaseDetailView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class CategoryList(BaseListCreateView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(BaseDetailView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class WarehouseList(BaseListCreateView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class WarehouseDetail(BaseDetailView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
