from django.test import TestCase

from task_manager.models import TaskType, Worker, Position, Task


class ModelTests(TestCase):
    def test_task_type_str(self) -> None:
        task_type = TaskType.objects.create(
            name="test",
        )
        self.assertEqual(
            str(task_type),
            task_type.name
        )

    def test_position_str(self) -> None:
        position = Position.objects.create(
            name="test",
        )
        self.assertEqual(
            str(position),
            position.name
        )

    def test_create_worker_with_position(self) -> None:
        position = Position.objects.create(
            name="test"
        )
        username = "test"
        password = "Test1234"
        worker = Worker.objects.create_user(
            username=username,
            password=password,
            position=position
        )
        self.assertEqual(worker.username, username)
        self.assertTrue(worker.check_password(password))
        self.assertEqual(worker.position, position)

    def test_task_str(self) -> None:
        position = Position.objects.create(
            name="test",
        )
        task_type = TaskType.objects.create(
            name="test"
        )
        name = "test"
        description = "test"
        deadline = "2015-04-04"
        is_completed=False
        username = "test"
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
        self.assertEqual(
            str(task),
            task.name
        )
