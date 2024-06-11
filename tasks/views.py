from django.shortcuts import render  # Import render function from Django
from rest_framework import generics  # Import generic views from DRF
from .serializers import *  # Import all serializers
from .models import *  # Import all models

# View for listing all ToDo items
class ListToDo(generics.ListAPIView):
    queryset = ToDo.objects.all()  # Get all ToDo objects
    serializer_class = ToDoSerializers  # Use ToDoSerializers

# View for retrieving and updating a single ToDo item
class DetailToDo(generics.RetrieveUpdateAPIView):
    queryset = ToDo.objects.all()  
    serializer_class = ToDoSerializers

# View for creating a new ToDo item
class CreateToDo(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializers

# View for retrieving and deleting a single ToDo item
class DeleteToDo(generics.RetrieveDestroyAPIView):
    queryset = ToDo.objects.all()  
    serializer_class = ToDoSerializers
