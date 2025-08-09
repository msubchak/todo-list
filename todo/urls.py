from django.urls import path

from todo.views import (
    TagListView,
    TagUpdateView,
    TagDeleteView,
    TagCreateView,
    TaskListView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
    task_status,
)

app_name = "todo_list"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/toggle/", task_status, name="task-status"),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),

]
