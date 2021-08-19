from django.conf.urls import (
    include,
    url,
)
from rest_framework import (
    routers,
)
from users.views import AuthView

v1_router = routers.SimpleRouter()

v1_urlpatterns = [
    url(r'', include(v1_router.urls)),
    url(r'^auth/$', AuthView.as_view()),
]


urlpatterns = [
    url(r'^api/v1/', include(v1_urlpatterns)),
]
