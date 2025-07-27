from dds.models import Status, Type, Category, SubCategory, Record
from datetime import date, timedelta
import random

if not (Status.objects.exists() and Type.objects.exists() and Category.objects.exists() and SubCategory.objects.exists()):
    print("Заполни сначала справочники через админку!")
else:
    statuses = list(Status.objects.all())
    types = list(Type.objects.all())
    categories = list(Category.objects.all())

    count = 7

    created = 0
    for _ in range(count):
        category = random.choice(categories)
        subcats = SubCategory.objects.filter(category=category)
        if not subcats.exists():
            continue

        Record.objects.create(
            date=date.today() - timedelta(days=random.randint(0, 60)),
            status=random.choice(statuses),
            type=category.type,
            category=category,
            subcategory=random.choice(list(subcats)),
            amount=round(random.uniform(100, 10000), 2),
            comment=random.choice([
                'Покупка сервера', 'Продажа аккаунта', 'Пополнение бюджета',
                'Оплата рекламы', 'Тестовая операция', 'Выплата сотруднику'
            ])
        )
        created += 1

    print(f"Добавлено {created} случайных записей.")
