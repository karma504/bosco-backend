import random
from datetime import date, timedelta

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Product


def products_list(request):
    products = Product.objects.all()
    return render(request, 'catalog/products.html', {'products': products})


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


def replenish_stock(request, count: int):
    catalog = {
        "Молочні продукти": ["Сир", "Молоко", "Йогурт", "Масло вершкове", "Кефір"],
        "Солодощі": ["Шоколад", "Печиво", "Цукерки", "Вафлі"],
        "Крупи": ["Гречка", "Рис", "Макарони", "Вівсянка"],
        "Випічка": ["Хліб", "Булочка", "Батон"],
        "Фрукти": ["Яблука", "Банани", "Груші"],
    }
    sample_weights = [100, 180, 200, 250, 350, 400, 500, 900, 1000]

    new_items = []
    for _ in range(count):
        category = random.choice(list(catalog.keys()))
        new_items.append(Product(
            name=random.choice(catalog[category]),
            category=category,
            weight_grams=random.choice(sample_weights),
            expiry_date=date.today() + timedelta(days=random.randint(5, 365)),
            price=round(random.uniform(20.0, 300.0), 2),
        ))

    Product.objects.bulk_create(new_items)

    return HttpResponse(
        f"<h2>Успішно додано {count} нових продуктів харчування!</h2>"
        f'<p><a href="/products">Повернутися до каталогу</a></p>'
    )