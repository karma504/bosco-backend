import random
from datetime import date, timedelta
from django.http import HttpResponse
from .models import Product


def products_list(request):
    products = Product.objects.all()

    rows = ""
    for p in products:
        rows += f"""
        <tr>
            <td>{p.id}</td>
            <td>{p.name}</td>
            <td>{p.category}</td>
            <td>{p.weight_grams} г</td>
            <td>{p.expiry_date.strftime('%d.%m.%Y')}</td>
            <td>{p.price} грн</td>
        </tr>
        """

    html = f"""
    <!DOCTYPE html>
    <html lang="uk">
    <head>
        <meta charset="UTF-8">
        <title>Продукти харчування - Склад</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 30px; background-color: #f4f6f9; }}
            h1 {{ color: #2c3e50; }}
            table {{ border-collapse: collapse; width: 100%; background: #ffffff; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
            th, td {{ border: 1px solid #dddddd; padding: 12px; text-align: left; }}
            th {{ background-color: #27ae60; color: white; }}
            tr:nth-child(even) {{ background-color: #f9f9f9; }}
        </style>
    </head>
    <body>
        <h1>Список продуктів харчування на складі</h1>
        <p>Усього найменувань: <strong>{products.count()}</strong></p>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Назва продукту</th>
                    <th>Категорія</th>
                    <th>Вага</th>
                    <th>Термін придатності</th>
                    <th>Ціна</th>
                </tr>
            </thead>
            <tbody>
                {rows}
            </tbody>
        </table>
    </body>
    </html>
    """
    return HttpResponse(html)

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