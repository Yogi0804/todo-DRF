from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
from .models import Task

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def apiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-details/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def taskDetail(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks,many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    print(serializer.is_valid())
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task,many=False,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    
    return Response("Successfully deleted a task")