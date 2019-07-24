from rest_framework import serializers
from .models import Task


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'price')


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'price', 'customer', 'executor', 'accomplished')


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'price', 'customer', 'executor', 'accomplished')


class TaskUpdateExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('executor', 'accomplished')
