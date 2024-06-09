from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    """
    A model representing a task.

    Attributes:
        created_at (DateTimeField): Timestamp when the task is created.
        user (ForeignKey): User who created the task.
        name (CharField): Name of the task.
        description (TextField): Description of the task.
        due_date (DateField): Due date for the task.
        assigned_to (ForeignKey): User to whom the task is assigned.
    """

    # Timestamp when the task is created
    created_at = models.DateTimeField(auto_now_add=True)

    # User who created the task
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="created_by"
        )
    
    # Task name
    name = models.CharField(max_length=200)

    # Task description
    description = models.TextField()

    # Due date for the task
    due_date = models.DateField()
    
    # User to whom the task is assigned
    assigned_to = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="assigned_to", 
        null=True, 
        blank=True
        )


    class Meta:
        """
        Meta options for the Task model.

        Attributes:
            ordering (list): Order tasks by due date.
        """

        # Order tasks by due date
        ordering = ['due_date']

    def __str__(self):
         # String representation of the task
        return self.name


