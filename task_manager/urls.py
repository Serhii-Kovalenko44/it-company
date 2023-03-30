from django.urls import path

from task_manager.views import (
    index,
    PositionListView,
    PositionDetailView,
    TaskTypeListView,
    WorkerListView,
    TaskListView,
    TaskDetailView, TaskCreateView, TaskUpdateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("position/", PositionListView.as_view(), name="position-list"),
    path("position/<int:pk>/", PositionDetailView.as_view(), name="position-detail"),
    path("task-type/", TaskTypeListView.as_view(), name="task-type-list"),
    path("worker/", WorkerListView.as_view(), name="worker-list"),
    path("task/", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),

]

app_name = "task_manager"
