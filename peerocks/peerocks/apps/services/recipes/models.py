from decimal import Decimal

from django.db.models import (
    PROTECT,
    CharField,
    ForeignKey,
    TextField, CASCADE, SET_NULL, DecimalField,
)
from utils.models import (
    ProjectModel,
)


class Recipe(ProjectModel):
    """
    Модель рецепта
    """

    title = CharField('Название', max_length=512)
    description = TextField('Описание')

    class Meta:
        db_table = 'recipes_recipe'
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class CookStep(ProjectModel):
    """
    Шаг приготовления блюда
    """

    title = CharField('Название', max_length=512)
    description = TextField('Описание')

    recipe = ForeignKey(Recipe, on_delete=CASCADE)

    next = ForeignKey('self', on_delete=SET_NULL, related_name='prev_step', blank=True, null=True)
    prev = ForeignKey('self', on_delete=PROTECT, related_name='next_step', blank=True, null=True)

    class Meta:
        db_table = 'recipes_cook_step'
        verbose_name = 'Шаг приготовления блюда'
        verbose_name_plural = 'Шаги приготовления блюд'


class RecipeProduct(ProjectModel):
    """
    Проодукт используемый в рецепте
    """

    recipe = ForeignKey(Recipe, verbose_name='Рецепт', on_delete=CASCADE)
    product = ForeignKey('products.Product', verbose_name='Продукт', on_delete=PROTECT)

    unit = ForeignKey('products.Unit', verbose_name='Единица измерения', on_delete=PROTECT)

    count = DecimalField('Количество', decimal_places=2, max_digits=6)

    class Meta:
        db_table = 'recipes_recipe_product'
        verbose_name = 'Продукт используемый в рецепте'
        verbose_name_plural = 'Продукты используемые в рецепте'


class RecipeFoodIntake(ProjectModel):
    """
    Принадлежность рецепта к тому или иному приему пищи
    """

    recipe = ForeignKey(Recipe, on_delete=CASCADE)
    food_intake = ForeignKey('common.FoodIntake', on_delete=PROTECT)

    class Meta:
        db_table = 'recipes_recipe_food_intake'
        verbose_name = 'Принадлежность рецепта к приему пищи'
        verbose_name_plural = 'Принадлежность рецептов к приемам пищи'


class CookStepRecipeProduct(ProjectModel):
    """
    Продукт используемый на шаге пприготовления блюда
    """

    cook_step = ForeignKey(CookStep, verbose_name='Шаг приготовления блюда', on_delete=PROTECT)
    recipe_product = ForeignKey(RecipeProduct, verbose_name='Продукт используемый в рецепте', on_delete=PROTECT)

    count = DecimalField('Количество', decimal_places=2, max_digits=6)

    class Meta:
        db_table = 'recipes_cook_step_recipe_product'
        verbose_name = 'Продукт используемый на шаге приготовления блюда'
        verbose_name_plural = 'Продукты используемые на шаге приготовления блюда'


class UserRecipe(ProjectModel):
    """
    Связь пользователя с рецептом. У рецепта могут быть соавторы, редакторы, поэтому необходима именно такая модель
    """

    user = ForeignKey('users.CustomUser', verbose_name='Пользователь', on_delete=CASCADE)
    recipe = ForeignKey(Recipe, verbose_name='Рецепт', on_delete=CASCADE)

    class Meta:
        db_table = 'recipes_user_recipe'
        verbose_name = 'Рецепт пользователя'
        verbose_name_plural = 'Рецепты пользователей'
