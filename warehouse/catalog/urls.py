from django.urls import path
from .views import products_list, replenish_stock

urlpatterns = [
    path('products', products_list, name='products_list'),
    path('replenish/<int:count>', replenish_stock, name='replenish_stock'),
]