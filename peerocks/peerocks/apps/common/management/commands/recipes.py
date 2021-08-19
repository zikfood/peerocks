from decimal import Decimal

from common.management.commands.products import get_products, get_units
from common.management.commands.users import get_users
from recipes.models import Recipe, CookStep, RecipeProduct, CookStepRecipeProduct, UserRecipe
from recommendations.models import Vote


def create_recipes():
    """
    Создание тестовых рецептов
    """

    recipe_1, _ = Recipe.objects.get_or_create(
        title='Рецепт 1',
        description='Описание рецепта 1',
    )

    recipe_2, _ = Recipe.objects.get_or_create(
        title='Рецепт 2',
        description='Описание рецепта 2',
    )

    recipe_3, _ = Recipe.objects.get_or_create(
        title='Рецепт 3',
        description='Описание рецепта 3',
    )

    recipe_4, _ = Recipe.objects.get_or_create(
        title='Рецепт 4',
        description='Описание рецепта 4',
    )

    recipe_5, _ = Recipe.objects.get_or_create(
        title='Рецепт 5',
        description='Описание рецепта 5',
    )

    recipe_1_step_1, _ = CookStep.objects.get_or_create(
        title='Рецепт 1 Шаг 1',
        description='Описание Рецепта 1 Шаг 1',
        recipe=recipe_1,
        next=None,
        prev=None,
    )

    recipe_1_step_2, _ = CookStep.objects.get_or_create(
        title='Рецепт 1 Шаг 2',
        description='Описание Рецепта 1 Шаг 2',
        recipe=recipe_1,
        next=None,
        prev=recipe_1_step_1,
    )

    recipe_1_step_1.next = recipe_1_step_2
    recipe_1_step_1.save()

    recipe_1_step_3, _ = CookStep.objects.get_or_create(
        title='Рецепт 1 Шаг 3',
        description='Описание Рецепта 1 Шаг 3',
        recipe=recipe_1,
        next=None,
        prev=recipe_1_step_2,
    )

    recipe_1_step_2.next = recipe_1_step_3
    recipe_1_step_2.save()

    recipe_2_step_1, _ = CookStep.objects.get_or_create(
        title='Рецепт 2 Шаг 1',
        description='Описание Рецепта 2 Шаг 1',
        recipe=recipe_2,
        next=None,
        prev=None,
    )

    recipe_2_step_2, _ = CookStep.objects.get_or_create(
        title='Рецепт 2 Шаг 2',
        description='Описание Рецепта 2 Шаг 2',
        recipe=recipe_2,
        next=None,
        prev=recipe_2_step_1,
    )

    recipe_2_step_1.next = recipe_2_step_2
    recipe_2_step_1.save()

    recipe_2_step_3, _ = CookStep.objects.get_or_create(
        title='Рецепт 2 Шаг 3',
        description='Описание Рецепта 2 Шаг 3',
        recipe=recipe_2,
        next=None,
        prev=recipe_2_step_2,
    )

    recipe_2_step_2.next = recipe_2_step_3
    recipe_2_step_2.save()

    recipe_3_step_1, _ = CookStep.objects.get_or_create(
        title='Рецепт 3 Шаг 1',
        description='Описание Рецепта 3 Шаг 1',
        recipe=recipe_3,
        next=None,
        prev=None,
    )

    recipe_3_step_2, _ = CookStep.objects.get_or_create(
        title='Рецепт 3 Шаг 2',
        description='Описание Рецепта 3 Шаг 2',
        recipe=recipe_3,
        next=None,
        prev=recipe_3_step_1,
    )

    recipe_3_step_1.next = recipe_3_step_2
    recipe_3_step_1.save()

    recipe_3_step_3, _ = CookStep.objects.get_or_create(
        title='Рецепт 3 Шаг 3',
        description='Описание Рецепта 3 Шаг 3',
        recipe=recipe_3,
        next=None,
        prev=recipe_3_step_2,
    )

    recipe_3_step_2.next = recipe_3_step_3
    recipe_3_step_2.save()

    recipe_3_step_4, _ = CookStep.objects.get_or_create(
        title='Рецепт 3 Шаг 4',
        description='Описание Рецепта 3 Шаг 4',
        recipe=recipe_3,
        next=None,
        prev=recipe_3_step_3,
    )

    recipe_3_step_3.next = recipe_3_step_4
    recipe_3_step_3.save()

    recipe_4_step_1, _ = CookStep.objects.get_or_create(
        title='Рецепт 4 Шаг 1',
        description='Описание Рецепта 4 Шаг 1',
        recipe=recipe_4,
        next=None,
        prev=None,
    )

    recipe_4_step_2, _ = CookStep.objects.get_or_create(
        title='Рецепт 4 Шаг 2',
        description='Описание Рецепта 4 Шаг 2',
        recipe=recipe_4,
        next=None,
        prev=recipe_4_step_1,
    )

    recipe_4_step_1.next = recipe_4_step_2
    recipe_4_step_1.save()

    recipe_4_step_3, _ = CookStep.objects.get_or_create(
        title='Рецепт 4 Шаг 3',
        description='Описание Рецепта 4 Шаг 3',
        recipe=recipe_4,
        next=None,
        prev=recipe_4_step_2,
    )

    recipe_4_step_2.next = recipe_4_step_3
    recipe_4_step_2.save()

    recipe_4_step_4, _ = CookStep.objects.get_or_create(
        title='Рецепт 4 Шаг 4',
        description='Описание Рецепта 4 Шаг 4',
        recipe=recipe_4,
        next=None,
        prev=recipe_4_step_3,
    )

    recipe_4_step_3.next = recipe_4_step_4
    recipe_4_step_3.save()

    recipe_4_step_5, _ = CookStep.objects.get_or_create(
        title='Рецепт 4 Шаг 5',
        description='Описание Рецепта 4 Шаг 5',
        recipe=recipe_4,
        next=None,
        prev=recipe_4_step_4,
    )

    recipe_4_step_4.next = recipe_4_step_5
    recipe_4_step_4.save()

    recipe_5_step_1, _ = CookStep.objects.get_or_create(
        title='Рецепт 5 Шаг 1',
        description='Описание Рецепта 5 Шаг 1',
        recipe=recipe_5,
        next=None,
        prev=None,
    )

    recipe_5_step_2, _ = CookStep.objects.get_or_create(
        title='Рецепт 5 Шаг 2',
        description='Описание Рецепта 5 Шаг 2',
        recipe=recipe_5,
        next=None,
        prev=recipe_5_step_1,
    )

    recipe_5_step_1.next = recipe_5_step_2
    recipe_5_step_1.save()

    recipe_5_step_3, _ = CookStep.objects.get_or_create(
        title='Рецепт 5 Шаг 3',
        description='Описание Рецепта 5 Шаг 3',
        recipe=recipe_5,
        next=None,
        prev=recipe_5_step_2,
    )

    recipe_5_step_2.next = recipe_5_step_3
    recipe_5_step_2.save()

    recipe_5_step_4, _ = CookStep.objects.get_or_create(
        title='Рецепт 5 Шаг 4',
        description='Описание Рецепта 5 Шаг 4',
        recipe=recipe_5,
        next=None,
        prev=recipe_5_step_3,
    )

    recipe_5_step_3.next = recipe_5_step_4
    recipe_5_step_3.save()

    recipe_5_step_5, _ = CookStep.objects.get_or_create(
        title='Рецепт 5 Шаг 5',
        description='Описание Рецепта 5 Шаг 5',
        recipe=recipe_5,
        next=None,
        prev=recipe_5_step_4,
    )

    recipe_5_step_4.next = recipe_5_step_5
    recipe_5_step_4.save()

    products = get_products()

    product_1 = products['Молоко']
    product_2 = products['Масло растительное']
    product_3 = products['Минеральная вода']
    product_4 = products['Соль']
    product_5 = products['Сахар']
    product_6 = products['Мясо говяжье']
    product_7 = products['Картофель']

    units = get_units()

    unit_1 = units['Литр']
    unit_2 = units['Грамм']

    recipe_1_product_1, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_1,
        product=product_1,
        unit=unit_1,
        count=Decimal(2),
    )

    recipe_1_product_2, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_1,
        product=product_2,
        unit=unit_1,
        count=Decimal(1),
    )

    recipe_1_product_3, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_1,
        product=product_3,
        unit=unit_1,
        count=Decimal(1),
    )

    recipe_1_product_5, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_1,
        product=product_5,
        unit=unit_2,
        count=Decimal(1),
    )

    recipe_1_product_6, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_1,
        product=product_6,
        unit=unit_2,
        count=Decimal(3),
    )

    recipe_1_step_1_product = CookStepRecipeProduct(
        cook_step=recipe_1_step_1,
        recipe_product=recipe_1_product_1,
        count=Decimal(1),
    )
    recipe_1_step_1_product = CookStepRecipeProduct(
        cook_step=recipe_1_step_1,
        recipe_product=recipe_1_product_2,
        count=Decimal(0.5),
    )
    recipe_1_step_2_product = CookStepRecipeProduct(
        cook_step=recipe_1_step_2,
        recipe_product=recipe_1_product_1,
        count=Decimal(1),
    )
    recipe_1_step_2_product = CookStepRecipeProduct(
        cook_step=recipe_1_step_2,
        recipe_product=recipe_1_product_2,
        count=Decimal(0.5),
    )
    recipe_1_step_3_product = CookStepRecipeProduct(
        cook_step=recipe_1_step_3,
        recipe_product=recipe_1_product_3,
        count=Decimal(1),
    )
    recipe_1_step_3_product = CookStepRecipeProduct(
        cook_step=recipe_1_step_3,
        recipe_product=recipe_1_product_5,
        count=Decimal(1),
    )
    recipe_1_step_3_product = CookStepRecipeProduct(
        cook_step=recipe_1_step_3,
        recipe_product=recipe_1_product_6,
        count=Decimal(3),
    )


    recipe_2_product_1, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_2,
        product=product_1,
        unit=unit_1,
        count=Decimal(4),
    )

    recipe_2_product_2, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_2,
        product=product_2,
        unit=unit_1,
        count=Decimal(2),
    )

    recipe_2_product_4, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_2,
        product=product_4,
        unit=unit_2,
        count=Decimal(20),
    )

    recipe_2_product_5, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_2,
        product=product_5,
        unit=unit_2,
        count=Decimal(10),
    )

    recipe_2_product_6, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_2,
        product=product_6,
        unit=unit_2,
        count=Decimal(500),
    )


    recipe_2_step_1_product = CookStepRecipeProduct(
        cook_step=recipe_2_step_1,
        recipe_product=recipe_2_product_1,
        count=Decimal(2),
    )
    recipe_2_step_1_product = CookStepRecipeProduct(
        cook_step=recipe_2_step_1,
        recipe_product=recipe_2_product_2,
        count=Decimal(2),
    )
    recipe_2_step_2_product = CookStepRecipeProduct(
        cook_step=recipe_2_step_2,
        recipe_product=recipe_2_product_1,
        count=Decimal(2),
    )
    recipe_2_step_2_product = CookStepRecipeProduct(
        cook_step=recipe_2_step_2,
        recipe_product=recipe_2_product_4,
        count=Decimal(20),
    )
    recipe_2_step_3_product = CookStepRecipeProduct(
        cook_step=recipe_2_step_3,
        recipe_product=recipe_2_product_5,
        count=Decimal(10),
    )
    recipe_2_step_3_product = CookStepRecipeProduct(
        cook_step=recipe_2_step_3,
        recipe_product=recipe_2_product_6,
        count=Decimal(500),
    )


    recipe_3_product_1, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_3,
        product=product_1,
        unit=unit_1,
        count=Decimal(5),
    )

    recipe_3_product_2, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_3,
        product=product_2,
        unit=unit_1,
        count=Decimal(3),
    )

    recipe_3_product_4, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_3,
        product=product_4,
        unit=unit_2,
        count=Decimal(22),
    )

    recipe_3_product_5, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_3,
        product=product_5,
        unit=unit_2,
        count=Decimal(12),
    )

    recipe_3_product_6, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_3,
        product=product_6,
        unit=unit_2,
        count=Decimal(1000),
    )

    recipe_3_product_7, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_3,
        product=product_7,
        unit=unit_2,
        count=Decimal(1000),
    )

    recipe_3_step_1_product = CookStepRecipeProduct(
        cook_step=recipe_3_step_1,
        recipe_product=recipe_3_product_1,
        count=Decimal(3),
    )
    recipe_3_step_1_product = CookStepRecipeProduct(
        cook_step=recipe_3_step_1,
        recipe_product=recipe_3_product_2,
        count=Decimal(2),
    )
    recipe_3_step_1_product = CookStepRecipeProduct(
        cook_step=recipe_3_step_1,
        recipe_product=recipe_3_product_4,
        count=Decimal(10),
    )
    recipe_3_step_2_product = CookStepRecipeProduct(
        cook_step=recipe_3_step_2,
        recipe_product=recipe_3_product_1,
        count=Decimal(2),
    )
    recipe_3_step_2_product = CookStepRecipeProduct(
        cook_step=recipe_3_step_2,
        recipe_product=recipe_3_product_2,
        count=Decimal(1),
    )
    recipe_3_step_3_product = CookStepRecipeProduct(
        cook_step=recipe_3_step_3,
        recipe_product=recipe_3_product_4,
        count=Decimal(12),
    )
    recipe_3_step_3_product = CookStepRecipeProduct(
        cook_step=recipe_3_step_3,
        recipe_product=recipe_3_product_5,
        count=Decimal(12),
    )
    recipe_3_step_4_product = CookStepRecipeProduct(
        cook_step=recipe_3_step_4,
        recipe_product=recipe_3_product_6,
        count=Decimal(1000),
    )
    recipe_3_step_4_product = CookStepRecipeProduct(
        cook_step=recipe_3_step_4,
        recipe_product=recipe_3_product_7,
        count=Decimal(1000),
    )


    recipe_4_product_1, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_4,
        product=product_1,
        unit=unit_1,
        count=Decimal(7),
    )

    recipe_4_product_2, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_4,
        product=product_2,
        unit=unit_1,
        count=Decimal(5),
    )

    recipe_4_product_4, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_4,
        product=product_4,
        unit=unit_2,
        count=Decimal(33),
    )

    recipe_4_product_5, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_4,
        product=product_5,
        unit=unit_2,
        count=Decimal(112),
    )

    recipe_4_product_6, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_4,
        product=product_6,
        unit=unit_2,
        count=Decimal(3000),
    )

    recipe_4_product_7, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_4,
        product=product_7,
        unit=unit_2,
        count=Decimal(3000),
    )


    recipe_4_step_1_product = CookStepRecipeProduct(
        cook_step=recipe_4_step_1,
        recipe_product=recipe_4_product_1,
        count=Decimal(7),
    )
    recipe_4_step_1_product = CookStepRecipeProduct(
        cook_step=recipe_4_step_1,
        recipe_product=recipe_4_product_2,
        count=Decimal(5),
    )
    recipe_4_step_2_product = CookStepRecipeProduct(
        cook_step=recipe_4_step_2,
        recipe_product=recipe_4_product_4,
        count=Decimal(33),
    )
    recipe_4_step_3_product = CookStepRecipeProduct(
        cook_step=recipe_4_step_3,
        recipe_product=recipe_4_product_5,
        count=Decimal(100),
    )
    recipe_4_step_3_product = CookStepRecipeProduct(
        cook_step=recipe_4_step_3,
        recipe_product=recipe_4_product_6,
        count=Decimal(3000),
    )
    recipe_4_step_4_product = CookStepRecipeProduct(
        cook_step=recipe_4_step_4,
        recipe_product=recipe_4_product_5,
        count=Decimal(12),
    )
    recipe_4_step_4_product = CookStepRecipeProduct(
        cook_step=recipe_4_step_4,
        recipe_product=recipe_4_product_7,
        count=Decimal(3000),
    )

    recipe_5_product_1, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_5,
        product=product_1,
        unit=unit_1,
        count=Decimal(12),
    )

    recipe_5_product_2, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_5,
        product=product_2,
        unit=unit_1,
        count=Decimal(13),
    )

    recipe_5_product_4, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_5,
        product=product_4,
        unit=unit_2,
        count=Decimal(38),
    )

    recipe_5_product_5, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_5,
        product=product_5,
        unit=unit_2,
        count=Decimal(212),
    )

    recipe_5_product_6, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_5,
        product=product_6,
        unit=unit_2,
        count=Decimal(3500),
    )

    recipe_5_product_7, _ = RecipeProduct.objects.get_or_create(
        recipe=recipe_5,
        product=product_7,
        unit=unit_2,
        count=Decimal(3500),
    )

    recipe_5_step_1_product = CookStepRecipeProduct(
        cook_step=recipe_5_step_1,
        recipe_product=recipe_5_product_1,
        count=Decimal(12),
    )
    recipe_5_step_1_product = CookStepRecipeProduct(
        cook_step=recipe_5_step_1,
        recipe_product=recipe_5_product_2,
        count=Decimal(7),
    )
    recipe_5_step_2_product = CookStepRecipeProduct(
        cook_step=recipe_5_step_2,
        recipe_product=recipe_5_product_4,
        count=Decimal(38),
    )
    recipe_5_step_3_product = CookStepRecipeProduct(
        cook_step=recipe_5_step_3,
        recipe_product=recipe_5_product_2,
        count=Decimal(6),
    )
    recipe_5_step_3_product = CookStepRecipeProduct(
        cook_step=recipe_5_step_3,
        recipe_product=recipe_5_product_5,
        count=Decimal(212),
    )
    recipe_5_step_4_product = CookStepRecipeProduct(
        cook_step=recipe_5_step_4,
        recipe_product=recipe_5_product_6,
        count=Decimal(3000),
    )
    recipe_5_step_5_product = CookStepRecipeProduct(
        cook_step=recipe_5_step_5,
        recipe_product=recipe_5_product_6,
        count=Decimal(500),
    )
    recipe_5_step_5_product = CookStepRecipeProduct(
        cook_step=recipe_5_step_5,
        recipe_product=recipe_5_product_7,
        count=Decimal(3500),
    )

    users = get_users()
    user_1 = users['user1@pee.rocks']
    user_2 = users['user2@pee.rocks']
    user_3 = users['user3@pee.rocks']
    user_4 = users['user4@pee.rocks']
    user_5 = users['user5@pee.rocks']


    Vote.objects.bulk_create([
        Vote(is_like=True, user=user_1, recipe=recipe_1),
        Vote(is_like=True, user=user_1, recipe=recipe_2),
        Vote(is_like=True, user=user_1, recipe=recipe_3),
        Vote(is_like=True, user=user_2, recipe=recipe_3),
        Vote(is_like=True, user=user_2, recipe=recipe_4),
        Vote(is_like=True, user=user_2, recipe=recipe_5),
        Vote(is_like=True, user=user_2, recipe=recipe_1),
    ])

    UserRecipe.objects.bulk_create([
        UserRecipe(user=user_4, recipe=recipe_1),
        UserRecipe(user=user_4, recipe=recipe_2),
        UserRecipe(user=user_4, recipe=recipe_3),
        UserRecipe(user=user_5, recipe=recipe_4),
        UserRecipe(user=user_5, recipe=recipe_5),
    ])
