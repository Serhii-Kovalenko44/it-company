from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class TaskType(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"


class Task(models.Model):
    PRIORITY = (
        (0, "Low"),
        (1, "Medium"),
        (2, "High"),
        (3, "Urgent"),
    )
    name = models.CharField(max_length=63)
    description = models.TextField()
    deadline = models.DateField
    is_completed = models.BooleanField()
    priority = models.IntegerField(choices=PRIORITY, default=0)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="task")

    def __str__(self) -> str:
        return self.name
