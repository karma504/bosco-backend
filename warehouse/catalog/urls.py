from django.urls import path
from .views import products_list, replenish_stock, add_product

urlpatterns = [
    path('products', products_list, name='products_list'),
    path('add', add_product, name='add_product'),
    path('replenish/<int:count>', replenish_stock, name='replenish_stock'),
]