from django.core.cache import cache
from .models import Product


def get_products_by_category(category_id):
    """
    Возвращает список продуктов в указанной категории.
    Использует низкоуровневое кеширование.
    """
    cache_key = f'category_{category_id}'
    products = cache.get(cache_key)

    if products is None:
        products = Product.objects.filter(category_id=category_id)
        cache.set(cache_key, products, 60 * 15)  # 15 минут
        print(f"🔹 Данные загружены из БД для категории {category_id}")
    else:
        print(f"💡 Данные получены из кеша для категории {category_id}")

    return products
