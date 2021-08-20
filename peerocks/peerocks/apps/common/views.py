import functools
import json
import time
from itertools import chain

from django.db import reset_queries, connection
from django.shortcuts import (
    render,
)
from django.views import (
    View,
)

from products.models import Product
from recipes.models import Recipe, UserRecipe, RecipeProduct, CookStep



def query_debugger(func):
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        reset_queries()

        start_queries = len(connection.queries)

        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        end_queries = len(connection.queries)

        print(f"Function : {func.__name__}")
        print(f"Number of Queries : {end_queries - start_queries}")
        print(f"Finished in : {(end - start):.2f}s")
        return result

    return inner_func



class Task1View(View):
    """
    Вывести список всех рецептов. Список должен содержать информацию о самом рецепте, авторе
    """

    @query_debugger
    def get(self, request, **kwargs):
        a = list(Recipe.objects.values_list('description', 'title', 'userrecipe__user'))

        return render(request, 'task.html', {'json_data': a})


class Task2View(View):
    """
    Вывести детальную информацию рецепта. Нужно получить информацию о самом рецепте, о шагах приготовления, списке
    необходимых продоктов для приготовления
    """

    @query_debugger
    def get(self, request, **kwargs):

        recipes = Recipe.objects.values_list('title', flat=True)
        recipe_info = dict()
        product_info = Product.objects.values('title', 'recipeproduct__recipe__title')
        cooksteps_info = CookStep.objects.values('title', 'description', 'recipe__title')

        for recipe in recipes:
            recipe_title = recipe.title
            recipe_info[recipe.title] = {
                "описание рецепта": Recipe.objects.values_list('description', flat=True).filter(title=recipe)}

            recipe_info[recipe.title]["продукт"] = []
            recipe_info[recipe.title]["этап"] = []

            products = product_info.filter(recipeproduct__recipe__title=recipe_title)
            for item in products:
                recipe_info[recipe.title]["продукт"].append(item.title)

            cooksteps = cooksteps_info.filter(recipe__title=recipe_title)
            for item in cooksteps:
                recipe_info[recipe.title]["этап"].update({item['title']: item['description']})


        return render(request, 'task.html', {'json_data': recipe_info})


class Task3View(View):
    """
    Вывести список рецептов, аналогичный заданию 1, только дополнительно должно быть выведено количество лайков. Сам
    список должен быть отсортирован по количеству лайков по убыванию
    """

    def get(self, request, **kwargs):
        data = {
            'response': 'some data task 3',
        }

        return render(request, 'task.html', {'json_data': json.dumps(data)})


class Task4View(View):
    """
    Вывести объединенный список TOP 3 авторов и TOP 3 голосующих с количеством рецептов для первых и количеством
    голосов для вторых. В выборке должен быть указан тип в отдельной колонкке - Автор или Пользователь.
    """

    def get(self, request, **kwargs):
        data = {
            'response': 'some data task 4',
        }

        return render(request, 'task.html', {'json_data': json.dumps(data)})


class Task5View(View):
    """
    Все продукты указаны для приготовления одной порции блюда. Необходимо вывести список необходимых продуктов для
    приготовления самостоятельно выбранного блюда в количестве 5-ти порций
    """

    def get(self, request, **kwargs):
        data = {
            'response': 'some data task 5',
        }

        return render(request, 'task.html', {'json_data': json.dumps(data)})




