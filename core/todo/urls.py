from django.urls import path
from .views import *

urlpatterns = [
    path("", TaskList.as_view(), name="task_list"),
    path("create/",TaskCreate.as_view(), name="create_task")
]
