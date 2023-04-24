from django.core.exceptions import ValidationError
from django.test import TestCase

from task_manager.forms import (
    WorkerCreationForm, WorkerUpdateDataForm,
)
from task_manager.models import Position


class FormTest(TestCase):
    def test_worker_creation_form_is_valid(self) -> None:
        position = Position.objects.create(
            name="test",
        )
        form_data = {
            "username": "test_username",
            "password1": "1qazcde3",
            "password2": "1qazcde3",
            "first_name": "Test first",
            "last_name": "Test last",
            "position": position,
        }
        form = WorkerCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


    def test_worker_update_data_form(self) -> None:
        position = Position.objects.create(
            name="test",
        )
        form_data = {
            "username": "username_test",
            "first_name": "first_test",
            "last_name": "last_test",
            "position": position,
        }
        form = WorkerUpdateDataForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)