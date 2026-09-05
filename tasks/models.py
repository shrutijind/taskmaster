from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)  # required
    description = models.TextField(blank=True, null=True)  # optional
    due_date = models.DateField(blank=True, null=True)  # optional
    status = models.CharField(
        max_length=20,
        choices=[("Pending", "Pending"), ("In Progress", "In Progress"), ("Completed", "Completed")],
        default="Pending"
    )
    priority = models.IntegerField(default=1)  # default value
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="tasks", blank=True, null=True)

    def __str__(self):
        return self.title
