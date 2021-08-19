from django.contrib.auth.hashers import (
    make_password,
)
from users.models import (
    CustomUser, Author,
)


def create_users():
    """
    Создание тестовых пользователей
    """
    CustomUser.objects.get_or_create(
        email='admin@pee.rocks',
        defaults=dict(
            password=make_password('qkyY31ys97OM'),
            is_staff=True,
            is_superuser=True,
            is_active=True,
            is_confirmed=True
        ),
    )

    CustomUser.objects.get_or_create(
        email='user1@pee.rocks',
        defaults=dict(
            password=make_password('qkyY31ys97OM'),
            is_staff=True,
            is_superuser=True,
            is_active=True,
            is_confirmed=True
        ),
    )

    CustomUser.objects.get_or_create(
        email='user2@pee.rocks',
        defaults=dict(
            password=make_password('qkyY31ys97OM'),
            is_staff=True,
            is_superuser=True,
            is_active=True,
            is_confirmed=True
        ),
    )

    CustomUser.objects.get_or_create(
        email='user3@pee.rocks',
        defaults=dict(
            password=make_password('qkyY31ys97OM'),
            is_staff=True,
            is_superuser=True,
            is_active=True,
            is_confirmed=True
        ),
    )

    Author.objects.get_or_create(
        email='user4@pee.rocks',
        defaults=dict(
            password=make_password('qkyY31ys97OM'),
            is_staff=True,
            is_superuser=True,
            is_active=True,
            is_confirmed=True
        ),
    )

    Author.objects.get_or_create(
        email='user5@pee.rocks',
        defaults=dict(
            password=make_password('qkyY31ys97OM'),
            is_staff=True,
            is_superuser=True,
            is_active=True,
            is_confirmed=True
        ),
    )


def get_users():
    """
    Получение тестовых пользователей
    """
    users = CustomUser.objects.iterator()

    return {user.email: user for user in users}
