from django.db.models import (
    PROTECT,
    CharField,
    ForeignKey,
    Model,
    TextField,
)
from utils.models import (
    ProjectModel,
)


class UnitGroup(ProjectModel):
    """
    Группа единиц измерения
    """

    title = CharField('Название', max_length=512)

    class Meta:
        db_table = 'product_unit_group'
        verbose_name = 'Группа единиц измерения'
        verbose_name_plural = 'Группы единиц измерения'


class Unit(ProjectModel):
    """
    Модель единицы измерения
    """

    title = CharField('Название', max_length=256)
    abbreviation = CharField('Аббревиатура', max_length=16)

    unit_group = ForeignKey(UnitGroup, on_delete=PROTECT)

    class Meta:
        db_table = 'products_unit'
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'


class Product(ProjectModel):
    """
    Модель продукта
    """

    title = CharField('Название', max_length=512)
    description = TextField('Описание', max_length=2048)

    unit_group = ForeignKey(UnitGroup, on_delete=PROTECT)

    class Meta:
        db_table = 'products_product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

