from typing import Optional

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from task_manager.forms import TaskForm, WorkerCreationForm, WorkerUpdateDataForm, TaskSearchForm, WorkerSearchForm
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

    def get_context_data(
        self,
        object_list: Optional[dict] = None,
        **kwargs
    ) -> dict:
        context = super(WorkerListView, self).get_context_data(**kwargs)
        context["search_form"] = WorkerSearchForm()

        return context

    def get_queryset(self) -> QuerySet:
        queryset = Worker.objects.all()
        form = WorkerSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("task_manager:worker-list")


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerUpdateDataForm
    success_url = reverse_lazy("task_manager:worker-list")


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("task_manager:worker-list")


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 5
    queryset = Task.objects.select_related("task_type")

    def get_context_data(
        self,
        object_list: Optional[dict] = None,
        **kwargs
    ) -> dict:
        context = super(TaskListView, self).get_context_data(**kwargs)
        context["search_form"] = TaskSearchForm()

        return context

    def get_queryset(self) -> QuerySet:
        queryset = Task.objects.all()
        form = TaskSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_manager:task-list")


@login_required
def toggle_assign_to_task(
    request: HttpRequest,
    pk: int
) -> HttpResponseRedirect:
    worker = Worker.objects.get(id=request.user.id)
    if (
        Task.objects.get(id=pk) in worker.task.all()
    ):  # probably could check if car exists
        worker.task.remove(pk)
    else:
        worker.task.add(pk)
    return HttpResponseRedirect(reverse_lazy("task_manager:task-detail", args=[pk]))
