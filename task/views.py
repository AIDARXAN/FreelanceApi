from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db import transaction
from django.shortcuts import get_object_or_404

from billing.views import Transaction
from task.models import Task
from .permissions import IsCustomer, IsOwner
from .serializers import TaskCreateSerializer, TaskDetailSerializer, TaskListSerializer


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer


class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskCreateSerializer
    permission_classes = (permissions.IsAuthenticated, IsCustomer)

    def post(self, request, *args, **kwargs):
        input_data = self.serializer_class(data=request.data)

        if input_data.is_valid():
            # TODO change logic => need to check customer balance validation for money;
            #  after delete if/else statement from billing.view which checks the user balance
            with transaction.atomic():
                Transaction.task_created_transaction(request.user, input_data.validated_data['price'])
            input_data.save(customer=request.user)

            return Response(status=status.HTTP_201_CREATED)

        return Response(input_data.errors, status=status.HTTP_401_UNAUTHORIZED)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    lookup_field = 'id'
    serializer_class = TaskDetailSerializer
    permission_classes = (permissions.IsAuthenticated, IsCustomer)

    @api_view(['POST', 'GET'])
    def completed(request, id):
        task = get_object_or_404(Task, id=id)

        with transaction.atomic():
            Transaction.task_completed_transaction(request.user, task.price, task=task)

        Task.objects.filter(id=id, executor=None).update(executor=request.user, accomplished=True)

        return Response({'message': 'Task Completed'}, status=status.HTTP_200_OK)
