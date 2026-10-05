import random
from datetime import date, timedelta
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def products_list(request):
    products = Product.objects.all()

    return render(request, 'catalog/products.html', {'products': products})

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

        product = Product(
            name=random.choice(catalog[category]),
            category=category,
            weight_grams=random.choice(sample_weights),
            expiry_date=date.today() + timedelta(days=random.randint(5, 365)),
            price=round(random.uniform(20.0, 300.0), 2)
        )
        new_items.append(product)

    Product.objects.bulk_create(new_items)

    return HttpResponse(
        f"<h2>Успішно додано {count} нових продуктів харчування!</h2>"
        f'<p><a href="/products">Повернутися до каталогу</a></p>'
    )