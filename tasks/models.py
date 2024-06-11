from django.db import models

# Define the ToDo model
class ToDo(models.Model):
    title = models.CharField(max_length=100, blank=False)  # Title of the ToDo
    description = models.TextField(blank=False)  # Description of the ToDo
    date = models.DateField(auto_now_add=True)  # Date created, auto set to current date
    completed = models.BooleanField(default=False)  # Status of completion
    
    def __str__(self):
        return self.title  # String representation of the model
