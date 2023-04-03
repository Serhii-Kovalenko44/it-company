from django.urls import path

from task_manager.views import (
    index,
    PositionListView,
    PositionDetailView,
    TaskTypeListView,
    WorkerListView,
    WorkerDetailView,
    WorkerCreateView,
    WorkerUpdateView,
    WorkerDeleteView,
    TaskListView,
    TaskDetailView,
    toggle_assign_to_task,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("position/", PositionListView.as_view(), name="position-list"),
    path("position/<int:pk>/", PositionDetailView.as_view(), name="position-detail"),
    path("task-type/", TaskTypeListView.as_view(), name="task-type-list"),
    path("worker/", WorkerListView.as_view(), name="worker-list"),
    path("worker/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("worker/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("worker/<int:pk>/update/", WorkerUpdateView.as_view(), name="worker-update"),
    path("worker/<int:pk>/delete/", WorkerDeleteView.as_view(), name="worker-delete"),
    path("task/", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),

]

app_name = "task_manager"
