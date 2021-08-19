from django.db.models import (
    CharField,
)
from utils.models import (
    ProjectModel,
)


class FoodIntake(ProjectModel):
    """
    Этап приема пищи
    """

    title = CharField('Название', max_length=256)

    class Meta:
        db_table = 'common_food_intake'
        verbose_name = 'Прием пищи'
        verbose_name_plural = 'Приемы пищи'

