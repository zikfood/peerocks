from rest_framework.exceptions import (
    APIException,
)


class NotUniqueException(Exception):
    pass


class UserIsNotActiveException(APIException):
    status_code = 403
    default_detail = 'This user not is active.'


class APICommonException(Exception):
    pass
