from common.views import (
    Task1View,
    Task2View,
    Task3View,
    Task4View,
    Task5View,
)
from django.urls import (
    re_path,
)


urlpatterns = [
    re_path(r'task-1/$', Task1View.as_view()),
    re_path(r'task-2/$', Task2View.as_view()),
    re_path(r'task-3/$', Task3View.as_view()),
    re_path(r'task-4/$', Task4View.as_view()),
    re_path(r'task-5/$', Task5View.as_view()),
]
