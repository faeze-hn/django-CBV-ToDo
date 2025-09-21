from django.urls import path

urlpattern = [
    path("", TaskList.as_view(), name="task_list"),
]
