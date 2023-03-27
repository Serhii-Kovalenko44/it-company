from django.urls import path

from task_manager.views import index, PositionListView, TaskTypeListView, WorkerListView, TaskListView

urlpatterns = [
    path("", index, name="index"),
    path("position/", PositionListView.as_view(), name="position-list"),
    path("task-type/", TaskTypeListView.as_view(), name="task-type-list"),
    path("worker/", WorkerListView.as_view(), name="worker-list"),
    path("task/", TaskListView.as_view(), name="task-list"),

]

app_name = "task_manager"
