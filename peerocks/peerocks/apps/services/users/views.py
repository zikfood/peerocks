from rest_framework.authtoken.models import (
    Token,
)
from rest_framework.response import (
    Response,
)
from rest_framework.views import (
    APIView,
)
from users.models import (
    CustomUser,
)
from users.serializers import (
    AuthSerializer,
)
from utils.exceptions import (
    APICommonException,
)


class AuthView(APIView):
    permission_classes = ()

    def post(self, *args, **kwargs):
        serializer = AuthSerializer(data=self.request.data)
        serializer.is_valid()
        try:
            user = CustomUser.objects.get(
                email=serializer.validated_data.get('email')
            )
        except CustomUser.DoesNotExist:
            raise APICommonException(dict(error_code=400001))

        if not user.check_password(serializer.validated_data.get('password')):
            raise APICommonException(dict(error_code=400002))

        token, is_created = Token.objects.get_or_create(user=user)

        data = {'token': token.key}

        return Response(
            data
        )