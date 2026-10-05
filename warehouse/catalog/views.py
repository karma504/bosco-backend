from django.contrib import messages
from django.shortcuts import render, redirect


def add_product(request):
    if request.method == "POST":
        Product.objects.create(
            name=request.POST["name"],
            category=request.POST["category"],
            weight_grams=request.POST["weight_grams"],
            expiry_date=request.POST["expiry_date"],
            price=request.POST["price"],
        )
        messages.success(request, "Продукт успішно додано!")
        return redirect("products_list")
    return render(request, "catalog/add_products.html")