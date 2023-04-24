from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.models import TaskType, Position, Task, Worker

TASKTYPE_URL = reverse("task_manager:task-type-list")
POSITION_URL = reverse("task_manager:position-list")
TASK_URL = reverse("task_manager:task-list")
WORKER_URL = reverse("task_manager:worker-list")


class PublicTaskTypeTests(TestCase):
    def test_login_required(self) -> None:
        res = self.client.get(TASKTYPE_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateTaskTypeTests(TestCase):
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

    def test_retrieve_task_type(self) -> None:
        TaskType.objects.create(name="Bug")
        TaskType.objects.create(name="QA")
        response = self.client.get(TASKTYPE_URL)

        task_type = TaskType.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["tasktype_list"]),
            list(task_type)
        )

        self.assertTemplateUsed(response, "task_manager/tasktype_list.html")


class PublicPositionTests(TestCase):
    def test_login_required(self) -> None:
        res = self.client.get(POSITION_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivatePositionTests(TestCase):
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

    def test_retrieve_position(self) -> None:
        Position.objects.create(name="Developer")
        Position.objects.create(name="QA")
        response = self.client.get(POSITION_URL)

        positions = Position.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["position_list"]),
            list(positions)
        )

        self.assertTemplateUsed(response, "task_manager/position_list.html")


class PublicWorkerTests(TestCase):
    def test_login_required(self) -> None:
        res = self.client.get(WORKER_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateWorkerTests(TestCase):
    def setUp(self) -> None:
        position = Position.objects.create(
            name="test"
        )
        self.user = get_user_model().objects.create_user(
            username="test",
            password="password123",
            position=position,
        )
        self.client.force_login(self.user)

    def test_retrieve_worker(self) -> None:
        position = Position.objects.create(
            name="test"
        )
        get_user_model().objects.create_user(
            username="test1",
            password="password123",
            position=position,
        )
        response = self.client.get(WORKER_URL)
        workers = Worker.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["worker_list"]),
            list(workers)
        )
        self.assertTemplateUsed(response, "task_manager/worker_list.html")


class PublicTaskTests(TestCase):
    def test_login_required(self) -> None:
        res = self.client.get(TASK_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateTaskTests(TestCase):
    def setUp(self) -> None:
        position = Position.objects.create(
            name="test"
        )
        self.user = get_user_model().objects.create_user(
            username="test",
            password="password123",
            position=position,
        )
        self.client.force_login(self.user)

    def test_retrieve_task(self) -> None:
        position = Position.objects.create(
            name="test",
        )
        task_type = TaskType.objects.create(
            name="test"
        )
        name = "test"
        description = "test"
        deadline = "2015-04-04"
        is_completed = False
        username = "test123"
        password = "Test1234"
        worker = Worker.objects.create_user(
            username=username,
            password=password,
            position=position
        )
        task = Task.objects.create(
            name=name,
            description=description,
            deadline=deadline,
            is_completed=is_completed,
            priority=1,
            task_type=task_type,
        )
        task.assignees.set([worker])
        response = self.client.get(TASK_URL)
        tasks = Task.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["task_list"]),
            list(tasks)
        )
        self.assertTemplateUsed(response, "task_manager/task_list.html")
