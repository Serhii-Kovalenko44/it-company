from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.models import Position, Task, Worker


class SearchFormTests(TestCase):
    def setUp(self) -> None:
        position = Position.objects.create(
            name="test"
        )
        self.user = get_user_model().objects.create_user(
            username="test1",
            password="password123",
            position=position,
        )

        self.client.force_login(self.user)

    def test_search_task_by_name(self) -> None:
        response = self.client.get(
            reverse("task_manager:task-list") + "?name=Fix"
        )
        self.assertEqual(
            list(response.context["task_list"]),
            list(Task.objects.filter(name__icontains="Fix"))
        )

    def test_search_worker_by_username(self) -> None:
        response = self.client.get(
            reverse("task_manager:worker-list") + "?username=User"
        )
        self.assertEqual(
            list(response.context["worker_list"]),
            list(Worker.objects.filter(username__icontains="User"))
        )