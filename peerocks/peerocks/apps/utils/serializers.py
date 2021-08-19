from rest_framework.serializers import (
    DateField,
    DateTimeField,
    ModelSerializer,
    Serializer,
)
from utils.exceptions import (
    APICommonException,
)


class CustomSerializer(Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def is_valid(self, raise_exception=False):
        if not super(CustomSerializer, self).is_valid():
            raise APICommonException(
                dict(
                    error_code=400001,
                    error_message=self.errors,
                )
            )

        return True


class CustomModelSerializer(ModelSerializer):
    def is_valid(self, raise_exception=False):
        if not super(CustomModelSerializer, self).is_valid():
            raise APICommonException(
                dict(
                    error_code=400001,
                    error_message=self.errors,
                )
            )

        return True


class CustomDateTimeField(DateTimeField):
    def to_representation(self, value):
        return value.strftime("%Y-%m-%dT%H:%M")


class CustomDateField(DateField):
    def to_representation(self, value):
        return value.strftime("%Y-%m-%d")
