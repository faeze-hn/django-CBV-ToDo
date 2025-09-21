from django.urls import path
from .views import (TaskList,TaskCreate,TaskDelete,TaskUpdate,TaskComplete)

urlpatterns = [
    path("", TaskList.as_view(), name="task_list"),
    path("create/",TaskCreate.as_view(), name="create_task"),
    path("update/",TaskUpdate.as_view(), name="update_task"),
    path("complete/",TaskComplete.as_view(), name="complete_task"),
    path("delete/",TaskDelete.as_view(), name="Delete_task"),
]