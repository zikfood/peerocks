from datetime import (
    datetime,
)

from django.contrib.auth.hashers import (
    make_password,
)
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db.models import (
    BooleanField,
    CharField,
    DateTimeField,
)
from pytz import (
    timezone,
)


class CustomUserManager(BaseUserManager):
    """
    Кастомный менеджер пользователя
    """

    def create_user(self, email=None, password=None):
        """
        Создание и сохранение пользователя с указанным паролем
        """
        user = self.model(
            is_staff=False,
            is_active=True,
            is_superuser=False,
            email=email,
            date_joined=datetime.utcnow().replace(tzinfo=timezone('UTC'))
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """
        Создание и сохранение суперпользователя с указанным паролем
        """
        user = self.model(
            email=email,
            password=make_password(password),
            is_staff=True,
            is_active=True,
            is_superuser=True,
            date_joined=datetime.utcnow().replace(tzinfo=timezone('UTC'))
        )
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Кастомный пользователь
    """

    email = CharField(max_length=32, unique=True, db_index=True, primary_key=True, verbose_name='email')

    is_staff = BooleanField(default=False, verbose_name='Является админом')
    date_joined = DateTimeField(default=datetime.utcnow, verbose_name='Дата создания')

    is_active = BooleanField(default=True, verbose_name='Активный')
    is_confirmed = BooleanField(default=False, verbose_name='Подтвержден')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __repr__(self):
        return self.get_username()

    def __str__(self):
        return self.__repr__()

    def get_username(self):
        return getattr(self, self.USERNAME_FIELD)

    def get_full_name(self):
        return f'{self.email}'

    def get_short_name(self):
        return f'{self.email}'

    def activate(self):
        self.is_active = True
        self.save()

    def confirm(self):
        self.is_confirmed = True
        self.save()


class Author(CustomUser):
    """
    Автор рецепта
    """

    class Meta:
        db_table = 'users_author'
        verbose_name = 'Автор рецепта'
        verbose_name_plural = 'Авторы рецепта'
