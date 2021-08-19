class BaseEnum:
    """
    Базовый класс перечислений
    """
    values = {}

    @classmethod
    def get_choices(cls):
        """
        Используется для ограничения полей ORM
        """
        return list(cls.values.items())

    @classmethod
    def get_value(cls, key):
        """
        Возвращает значение по ключу
        """
        return cls.values[key]
