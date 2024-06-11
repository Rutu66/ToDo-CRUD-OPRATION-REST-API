from rest_framework import serializers
from .models import ToDo  # Import the ToDo model

# Define the ToDo serializer
class ToDoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ToDo  # Specify the model
        fields = ['id', 'title', 'description', 'date', 'completed']  # Specify the fields
