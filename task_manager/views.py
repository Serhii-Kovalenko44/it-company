from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from task_manager.models import TaskType, Position, Worker, Task


@login_required
def index(request) -> render:
    num_task_type = TaskType.objects.count()
    num_position = Position.objects.count()
    num_worker = Worker.objects.count()
    num_task = Task.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_task_type": num_task_type,
        "num_position": num_position,
        "num_worker": num_worker,
        "num_task": num_task,
        "num_visits": num_visits + 1,
    }

    return render(request, "task_manager/index.html", context=context)


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    paginate_by = 5
    queryset = Position.objects.all()


class PositionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Position


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    paginate_by = 5
    queryset = TaskType.objects.all()


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    queryset = Worker.objects.all()
    paginate_by = 5


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 5
    queryset = Task.objects.select_related("task_type")
