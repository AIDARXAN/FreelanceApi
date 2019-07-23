from django.shortcuts import render, get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db import transaction

from task.models import Task
from .permissions import IsCustomerUser, IsOwnerTask
from .serializers import TaskCreateSerializer, TaskDetailSerializer, TaskListSerializer, TaskUpdateExecutorSerializer


class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskCreateSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerTask)

    def post(self, request, *args, **kwargs):
        input_data = self.serializer_class(data=request.data)

        if input_data.is_vaild():
            input_data.save(customer=request.user)

            return Response(status=status.HTTP_201_CREATED)

        return Response(input_data.errors, status=status.HTTP_401_UNAUTHORIZED)


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer


class TaskDetailView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    lookup_field = 'id'
    serializer_class = TaskDetailSerializer
    permission_classes = (permissions.IsAuthenticated, IsCustomerUser)

    @api_view(['POST', 'GET'])
    def accept(self, request, id):
        task = get_object_or_404(Task, id=id)

        with transaction.atomic():
            request.user.update_balance(task.price, task=task)

        Task.objects.filter(id=id, executor=None).update(executor=request.user, accomplished=True)

        return Response({'message': 'Accept'}, status=status.HTTP_200_OK)
