import json
from pathlib import Path
from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Загружает тестовые данные из фикстур (предварительно очищая БД)'

    def handle(self, *args, **kwargs):
        fixtures_dir = Path(__file__).resolve().parent.parent.parent / 'fixtures'
        categories_fixture = fixtures_dir / 'categories.json'
        products_fixture = fixtures_dir / 'products.json'

        self.stdout.write('🔄 Начинаю загрузку тестовых данных...')

        # Очищаем существующие данные
        self.stdout.write('🗑️  Удаляю существующие категории и продукты...')
        Category.objects.all().delete()
        Product.objects.all().delete()
        self.stdout.write('✅ Существующие данные удалены.')

        # Загружаем категории напрямую из JSON
        if categories_fixture.exists():
            self.stdout.write(f'📂 Загружаю категории из {categories_fixture}...')
            with open(categories_fixture, 'r', encoding='utf-8') as f:
                data = json.load(f)
            count = 0
            for item in data:
                Category.objects.create(
                    id=item['pk'],
                    name=item['fields']['name'],
                    description=item['fields']['description']
                )
                count += 1
            self.stdout.write(f'✅ Загружено категорий: {count}')
        else:
            self.stdout.write(self.style.ERROR(f'❌ Файл {categories_fixture} не найден!'))

        # Загружаем продукты напрямую из JSON
        if products_fixture.exists():
            self.stdout.write(f'📂 Загружаю продукты из {products_fixture}...')
            with open(products_fixture, 'r', encoding='utf-8') as f:
                data = json.load(f)
            count = 0
            for item in data:
                # Находим категорию по ID
                category_id = item['fields']['category']
                category = Category.objects.get(id=category_id)
                Product.objects.create(
                    id=item['pk'],
                    name=item['fields']['name'],
                    description=item['fields']['description'],
                    category=category,
                    price=item['fields']['price'],
                    image=item['fields'].get('image', '')
                )
                count += 1
            self.stdout.write(f'✅ Загружено продуктов: {count}')
        else:
            self.stdout.write(self.style.ERROR(f'❌ Файл {products_fixture} не найден!'))

        self.stdout.write(self.style.SUCCESS('🎉 Загрузка тестовых данных завершена!'))

