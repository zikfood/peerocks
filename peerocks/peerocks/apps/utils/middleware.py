import json

from django.conf import (
    settings,
)
from django.http import (
    HttpResponse,
)
from django.utils.deprecation import (
    MiddlewareMixin,
)

from utils.exceptions import (
    APICommonException,
)


class ApiExceptionMiddleware(MiddlewareMixin):
    """
    Перехватывает и обрабатывает исключение
    """

    @staticmethod
    def process_exception(request, exception):
        if isinstance(exception, APICommonException):
            response = None

            try:
                error_code = exception.args[0]['error_code']
            except IndexError:
                response = HttpResponse(status=500)
            else:
                error_message = (
                    exception.args[0]['error_message'] if
                    'error_message' in exception.args[0] else
                    str(settings.ERRORS_CODES[error_code])
                )

                response = HttpResponse(status=400, content=json.dumps(
                    dict(
                        error_message=error_message,
                        error_code=error_code
                    )
                ))

            return response
