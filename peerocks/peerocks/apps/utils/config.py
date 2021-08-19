from configparser import (
    ConfigParser,
)


class ProjectConfig:
    """
    Обертка над парсером параметров конфигурации
    """

    def __init__(self, filenames=None, defaults=None):
        self.parser = ConfigParser()

        if filenames:
            self.parser.read(filenames)

        self.defaults = defaults or {}

    def read(self, filenames):
        """
        Загружает конфигурацию из файла(ов) filenames
        """
        self.parser = ConfigParser()
        self.parser.read(filenames)

    def set_defaults(self, defaults):
        """
        Устанавливает параметры проекта по умолчанию
        """
        self.defaults = defaults

    def items(self, section):
        """
        Возвращает список кортежей (key, value) из указанной секции.
        В случае, если такой секции нет, то возвращается пустой список.
        """
        if self.parser.has_section(section):
            result = self.parser.items(section)
        else:
            result = []

        return result

    def get(self, section, option):
        """
        Безопастно возвращает значение конфигурационного параметра option
        из раздела section
        """
        if self.parser.has_section(section) and self.parser.has_option(section, option):
            value = self.parser.get(section, option).strip()

            if value:
                result = value
            else:
                result = self.defaults[(section, option)]

        elif (section, option) in self.defaults:
            result = self.defaults[(section, option)]
        else:
            result = ''

        return result

    def get_bool(self, section, option):
        """
        Безопастно возвращает булево из конфига
        """
        value = self.get(section, option)

        if isinstance(value, str):
            value = value.upper() == 'TRUE'

        return bool(value)

    def get_int(self, section, option):
        """
        Безопасно возвращает целое число из конфига
        """
        value = self.get(section, option)

        if isinstance(value, str):
            try:
                value = int(value)
            except ValueError:
                value = 0

        return value

    def get_uint(self, section, option):
        """
        Безопасно возвращает положительное целое число из конфига
        """
        value = self.get_int(section, option)

        if value < 0:
            value = 0

        return value

    def get_list(self, section, option):
        """
        Возвращает список объектов из строки
        """
        raw_str = self.get(section, option)
        if raw_str:
            result = [x.strip() for x in raw_str.split(',')]
        else:
            result = []

        return result

