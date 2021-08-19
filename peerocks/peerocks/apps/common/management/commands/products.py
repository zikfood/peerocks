from products.models import (
    Product,
    Unit,
    UnitGroup,
)


def create_products():
    """
    Создание тестовых данных приложения products
    """

    unit_group_1, _ = UnitGroup.objects.get_or_create(
        title='Объем',
    )

    unit_group_2, _ = UnitGroup.objects.get_or_create(
        title='Вес',
    )

    unit_group_3, _ = UnitGroup.objects.get_or_create(
        title='Длина',
    )

    Unit.objects.get_or_create(
        title='Милилитр',
        abbreviation='мл',
        unit_group=unit_group_1,
    )

    Unit.objects.get_or_create(
        title='Литр',
        abbreviation='л',
        unit_group=unit_group_1,
    )

    Unit.objects.get_or_create(
        title='Грамм',
        abbreviation='г',
        unit_group=unit_group_2,
    )

    Unit.objects.get_or_create(
        title='Килограмм',
        abbreviation='кг',
        unit_group=unit_group_2,
    )

    Unit.objects.get_or_create(
        title='Сантиметр',
        abbreviation='см',
        unit_group=unit_group_3,
    )

    Unit.objects.get_or_create(
        title='Метр',
        abbreviation='м',
        unit_group=unit_group_3,
    )

    Product.objects.get_or_create(
        title='Молоко',
        description='Молоко 3.2%',
        unit_group=unit_group_1,
    )

    Product.objects.get_or_create(
        title='Масло растительное',
        description='Масло растительное рафинированное',
        unit_group=unit_group_1,
    )

    Product.objects.get_or_create(
        title='Минеральная вода',
        description='Минеральная вода',
        unit_group=unit_group_1,
    )

    Product.objects.get_or_create(
        title='Соль',
        description='Соль',
        unit_group=unit_group_2,
    )

    Product.objects.get_or_create(
        title='Сахар',
        description='Сахар',
        unit_group=unit_group_2,
    )

    Product.objects.get_or_create(
        title='Мясо говяжье',
        description='Мясо говяжье',
        unit_group=unit_group_2,
    )

    Product.objects.get_or_create(
        title='Картофель',
        description='Картофель',
        unit_group=unit_group_2,
    )


def get_units():
    """
    Получение единиц измерения
    """
    units = Unit.objects.iterator()

    return {unit.title: unit for unit in units}


def get_products():
    """
    Получение продуктов
    """
    products = Product.objects.iterator()

    return {product.title: product for product in products}
