from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodosSerializers
from todo_app.models import Todos

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'index' : '/',
        'about' : '/about/',
        'create' : '/create/',
        'update' : '/update/<str:pk>/',
        'yes_finish' : '/yes_finish/<str:pk>/',
        'no_finish' : '/no_finish/<str:pk>/',
        'delete' : '/delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def index(request):
    todo_list = Todos.objects.all()
    serializer = TodosSerializers(todo_list, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    serializer = TodosSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def update(request, pk):
    todo_update = Todos.objects.get(id = pk)
    serializer = TodosSerializers(instance=todo_update, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def yes_finish(request, pk):
    todo_yes_finish = Todos.objects.get(id = pk)
    serializer = TodosSerializers(instance=todo_yes_finish, data=request.data)
    if todo_yes_finish.finished(True):
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def no_finish(request, pk):
    todo_no_finish = Todos.objects.get(id = pk)
    serializer = TodosSerializers(instance=todo_no_finish, data=request.data)
    if todo_no_finish.finished(False):
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request, pk):
    todo_delete = Todos.objects.get(id = pk)
    todo_delete.delete()
    return Response("Başarıyla silindi.")



