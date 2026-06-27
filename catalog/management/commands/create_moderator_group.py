from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product

class Command(BaseCommand):
    help = 'Создаёт группу "Модератор продуктов" и назначает права'

    def handle(self, *args, **options):
        # Получаем тип контента для модели Product
        content_type = ContentType.objects.get_for_model(Product)

        # Получаем или создаём право can_unpublish_product
        unpublish_perm, _ = Permission.objects.get_or_create(
            codename='can_unpublish_product',
            name='Может отменять публикацию продукта',
            content_type=content_type,
        )

        # Получаем стандартное право на удаление
        delete_perm = Permission.objects.get(
            codename='delete_product',
            content_type=content_type,
        )

        # Создаём или получаем группу
        group, created = Group.objects.get_or_create(name='Модератор продуктов')

        # Назначаем права группе
        group.permissions.add(unpublish_perm, delete_perm)

        if created:
            self.stdout.write(self.style.SUCCESS('✅ Группа "Модератор продуктов" создана'))
        else:
            self.stdout.write(self.style.SUCCESS('ℹ️ Группа "Модератор продуктов" уже существует'))

        self.stdout.write(self.style.SUCCESS('✅ Права назначены группе'))
