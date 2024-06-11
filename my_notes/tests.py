from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task
from datetime import datetime


class TaskModelTest(TestCase):
    """
    A test case for checking a task.
    """
    def setUp(self):
        """
        Set up a user and a task for testing.
        """
        self.user = User.objects.create_user(
            username="TestUser", 
            password="password"
            )
        self.task = Task.objects.create(
            name="Test Note", 
            description="This is a test note",
            due_date=datetime.now(),
            user=self.user
            )
        
    def test_task_has_name(self):
        """
        Test that the task has the correct name.
        """
        task = Task.objects.get(id=self.task.id)
        self.assertEqual(task.name, "Test Note")

    def test_task_has_description(self):
        """
        Test that the task has the correct description.
        """
        task = Task.objects.get(id=self.task.id)
        self.assertEqual(task.description, "This is a test note")


class TaskViewTest(TestCase):
    """
    A test case for viewing a task.
    """
    def setUp(self):
        """
        Set up a user and a task for testing views.
        """
        self.user = User.objects.create_user(
            username="TestUser", 
            password="password"
            )
        self.task = Task.objects.create(
            name="Test Note", 
            description="This is a test note",
            due_date=datetime.now(),
            user=self.user
            )

    def test_task_list_view(self):
        """
        Test that the task list view returns a successful response and 
        contains the task name for the authenticated user.
        """
        self.client.login(username="TestUser", password="password")
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task.name)     

    def test_task_detail_view(self):
        """
        Test that the task detail view returns a successful response and 
        contains the task details for the authenticated user.
        """
        self.client.login(username="TestUser", password="password")
        task = Task.objects.get(id=self.task.id)
        response = self.client.get(reverse('task', args=[str(task.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task.name)


class TaskDeleteTest(TestCase):
    """
    A test case for deleting a task.
    """
    def setUp(self):
        """
        Set up a test user and a test task for deletion.
        """
        self.user = User.objects.create_user(
            username="TestUser", 
            password="password"
            )
        self.task = Task.objects.create(
            name="Test Note", 
            description="This is a test note",
            due_date=datetime.now(),
            user=self.user
        )
    
    def test_delete_task(self):
        """
        Test deleting a task.
        """
        self.client.login(username="TestUser", password="password")
        task_to_delete = Task.objects.get(id=self.task.id)
        response = self.client.delete(reverse(
            'delete_task', 
            args=[str(task_to_delete.id)]
            )
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())


class UpdateTaskTest(TestCase):
    """
    A test case for updating a task.
    """
    def setUp(self):
        """
        Set up a test user and a test task for updating.
        """
        self.user = User.objects.create_user(
            username="TestUser", 
            password="password"
        )

        self.task = Task.objects.create(
            name="Test Note", 
            description="This is a test note",
            due_date=datetime.now(),
            user=self.user,
            assigned_to=self.user
        )
    
    def test_update_task(self):
        """
        Test updating a task.
        """
        self.client.login(username="TestUser", password="password")
        task_to_update = Task.objects.get(id=self.task.id)
        updated_name = "Updated Note"
        updated_description = "This is an updated test note"
        updated_due_date = datetime.date(
            datetime.strptime("2099-01-01", "%Y-%m-%d"))

        # Updated task data
        updated_data = {
            "name": updated_name,
            "description": updated_description,
            "due_date": updated_due_date,
            "assigned_to": task_to_update.assigned_to.id
        }

        # A POST request to update the task
        response = self.client.post(reverse(
            'update_task', 
            args=[task_to_update.id]), 
            data=updated_data
            )
        
        # Checking if the task has been updated successfully
        self.assertEqual(response.status_code, 302)  
        updated_task = Task.objects.get(id=task_to_update.id)
        self.assertEqual(updated_task.name, updated_name)
        self.assertEqual(updated_task.description, updated_description)
        self.assertEqual(updated_task.due_date, updated_due_date)
        self.assertEqual(updated_task.assigned_to, self.user)


     

