from datetime import (
    datetime,
)

from django.contrib.auth.models import (
    User,
)
from rest_framework import (
    status,
)
from rest_framework.reverse import (
    reverse,
)
from rest_framework.test import (
    APITestCase,
)
from utils.enums import (
    BaseEnum,
)


class DataTypeEnum(BaseEnum):
    STRING = 'string'
    FIELD = 'field'
    DATE = 'date'
    TIME = 'time'


class APIWithAuthenticationTestCase(APITestCase):
    login = 'test_user'
    password = '12345'

    def create_user(self, login, password):
        """
        Создание пользователя
        """
        return User.objects.create_user(
            username=login,
            password=password,
        )

    def authenticate(self, login, password):
        """
        Авторизация
        """
        self.assertTrue(
            self.client.login(
                username=login,
                password=password,
            )
        )

    def setUp(self) -> None:
        super().setUp()

        self.create_user(
            self.login,
            self.password,
        )

        self.authenticate(
            self.login,
            self.password,
        )

        response = self.client.get(
            reverse('openapi-schema')
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )


class CRUDAPITestCase(APIWithAuthenticationTestCase):
    route_url = None
    model = None
    test_data = None
    test_data_types = None
    instance_data = None

    def setUp(self) -> None:
        """
        Настройки теста, формирование тестовых данных
        """
        super().setUp()

        if not self.model or not self.route_url:
            self.skipTest('self.model or self.route_url not implemented!')

        self.model_fields_related_models = {
            f.name: f.related_model
            for f in self.model._meta.fields
            if f.related_model
        }

        self.detail_url_name = f'{self.route_url}-detail'
        self.list_url_name = f'{self.route_url}-list'

        self.test_data = {}
        self.test_data_types = {}
        self.instance_data = {}

        options_response = self.client.options(
            reverse(self.list_url_name),
        )
        fields = options_response.json()['actions']['POST']

        for field_name, field_specs in fields.items():
            self.fill_test_data_field(
                field_name,
                field_specs,
            )

    def get_changed_test_data(self):
        """
        Изменение тестовых данных
        """
        data = self.test_data.copy()

        for idx, (field_name, value) in enumerate(data.items()):
            self.change_test_data(data, field_name, value, idx)

        return data

    def test_create_item(self):
        """
        Добавление записи
        """
        existed_ids = list(self.model.objects.values_list('id', flat=True))
        total = len(existed_ids)

        response = self.client.post(
            reverse(self.list_url_name),
            data=self.test_data,
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.model.objects.count(), total + 1)

        created_item = self.model.objects.exclude(id__in=existed_ids).first()

        self.check_created_item(created_item)

    def check_created_item(self, created_item):
        """
        Проверка созданной записи
        """
        for field, value in self.instance_data.items():
            self.assertEqual(getattr(created_item, field), value)

    def test_list_item(self):
        """
        Получение списка записей
        """
        self.prepare_items_list()

        response = self.client.get(
            reverse(self.list_url_name),
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.model.objects.count(), response.json()['count'])

    def prepare_items_list(self, count=4):
        """
        Плодготовка набора записей
        """
        for idx in range(count):
            self.model.objects.create(**self.instance_data)

    def test_get_item(self):
        """
        Получение записи
        """
        item = self.model.objects.create(**self.instance_data)

        response = self.client.get(
            reverse(self.detail_url_name, (item.id,)),
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for field, value in self.test_data.items():
            self.assertEqual(value, response.json()[field])

    def test_update_item(self):
        """
        Изменение записи - метод put
        """
        item = self.model.objects.create(**self.instance_data)

        changed_data = self.get_changed_test_data()

        response = self.client.put(
            reverse(self.detail_url_name, (item.id,)),
            data=changed_data,
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for field, value in changed_data.items():
            self.assertEqual(response.json()[field], value)

    def test_patch_item(self):
        """
        Изменение записи - метод patch
        """
        item = self.model.objects.create(**self.instance_data)

        changed_data = self.get_changed_test_data()

        response = self.client.patch(
            reverse(self.detail_url_name, (item.id,)),
            data=changed_data,
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for field, value in changed_data.items():
            self.assertEqual(response.json()[field], value)

    def test_delete_item(self):
        """
        Удаление записи
        """
        item = self.model.objects.create(**self.instance_data)
        total = self.model.objects.count()

        response = self.client.delete(
            reverse(self.detail_url_name, (item.id,)),
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.model.objects.count(), total - 1)

    def fill_test_data_field(self, field_name, field_specs):
        """
        Заполнение поля тестовых данных тестовым значением
        """
        self.test_data_types[field_name] = {
            'type': field_specs.get('type'),
            'required': field_specs.get('required'),
        }

        if not field_specs['required']:
            return

        value = ''

        if field_name in self.model_fields_related_models:
            related_model = self.model_fields_related_models.get(field_name)
            instance = related_model.objects.first()
            if not instance:
                instance = related_model.objects.create()
            self.test_data[field_name] = instance.id
            self.instance_data[field_name] = instance
        else:
            if field_specs['type'] in {
                DataTypeEnum.STRING,
                DataTypeEnum.FIELD,
            }:
                value = f'Тестовое {field_specs["label"]}'
                self.instance_data[field_name] = value
            elif field_specs['type'] == DataTypeEnum.DATE:
                date = datetime.now()
                value = date.strftime('%Y-%m-%d')
                self.instance_data[field_name] = date.date()
            elif field_specs['type'] == DataTypeEnum.TIME:
                date = datetime.now().replace(microsecond=0)
                value = date.strftime('%H:%M:%S')
                self.instance_data[field_name] = date.time()

            self.test_data[field_name] = value

    def change_test_data(self, data, field_name, value, idx):
        """
        Изменение тестовых данных
        """
        if field_name in self.model_fields_related_models:
            return

        if self.test_data_types[field_name]['type'] in {
            DataTypeEnum.STRING,
            DataTypeEnum.FIELD,
        }:
            data[field_name] = f'{value} - {idx}'
