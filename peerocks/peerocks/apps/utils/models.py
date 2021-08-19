from django.db import (
    models,
)

from utils.classes import (
    ProjectClass,
)


class ProjectModelMetaClass(type(models.Model), type(ProjectClass)):
    """
    Базовая абстрактная модель для проекта
    """


class ProjectModel(ProjectClass, models.Model, metaclass=ProjectModelMetaClass):
    """
    Базовая модель для проекта
    """
    class Meta:
        abstract = True
