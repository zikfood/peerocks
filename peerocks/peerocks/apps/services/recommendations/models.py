from django.db.models import (
    CASCADE,
    BooleanField,
    ForeignKey,
)
from utils.models import (
    ProjectModel,
)


class Vote(ProjectModel):
    """
    Отметка пользователя
    """

    is_like = BooleanField('Положительная отметка пользователя', default=False)

    user = ForeignKey('users.CustomUser', verbose_name='Пользователь', on_delete=CASCADE)
    recipe = ForeignKey('recipes.Recipe', verbose_name='Рецепт', on_delete=CASCADE)

    class Meta:
        db_table = 'recommendations_vote'
        verbose_name = 'Отметка пользователя'
        verbose_name_plural = 'Отметки пользователей'
