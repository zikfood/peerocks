from rest_framework.serializers import (
    CharField,
    EmailField,
)
from utils.serializers import (
    CustomSerializer,
)


class AuthSerializer(CustomSerializer):
    email = EmailField(max_length=32)
    password = CharField(max_length=64)




