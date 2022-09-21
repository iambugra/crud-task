from rest_framework.response import Response
from rest_framework.decorators import api_view
from task.models import Task
from .serializers import TaskSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def readTask(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createTask(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def updateTask(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def deleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return Response(status=status.HTTP_200_OK)