from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db import transaction
from django.shortcuts import get_object_or_404

from billing.models import Balance
from task.models import Task
from .permissions import IsCustomer, IsOwner
from .serializers import TaskCreateSerializer, TaskDetailSerializer, TaskListSerializer, TaskUpdateExecutorSerializer


class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskCreateSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def post(self, request, *args, **kwargs):
        input_data = self.serializer_class(data=request.data)

        if input_data.is_valid():
            input_data.save(customer=request.user)

            return Response(status=status.HTTP_201_CREATED)

        return Response(input_data.errors, status=status.HTTP_401_UNAUTHORIZED)


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    lookup_field = 'id'
    serializer_class = TaskDetailSerializer
    permission_classes = (permissions.IsAuthenticated, IsCustomer)

    @api_view(['POST', 'GET'])
    def accept(request, id):
        task = get_object_or_404(Task, id=id)

        with transaction.atomic():
            Balance.update_balance(request.user, task.price, task=task)

        Task.objects.filter(id=id, executor=None).update(executor=request.user, accomplished=True)

        return Response({'message': 'Accept'}, status=status.HTTP_200_OK)
