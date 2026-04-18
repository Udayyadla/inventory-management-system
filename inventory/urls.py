from django.urls import path
from .views import (
ProductList, ProductDetail,
SupplierList, SupplierDetail,
CategoryList, CategoryDetail,
InventoryList, InventoryDetail,
StockMovementList, StockMovementDetail,
WarehouseList, WarehouseDetail

    )


urlpatterns = [
# Product
path('products/',ProductList.as_view(),name="product-list"),
path("products/<int:pk>/", ProductDetail.as_view(),name="product-detail"),


# stock movement
path("stock-movements/",StockMovementList.as_view(),name="stock-movement-list"),
path("stock-movements/<int:pk>/", StockMovementDetail.as_view(), name= "stock-movement-detail"),

    ]