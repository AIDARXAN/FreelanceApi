from django.urls import path
from .views import *

urlpatterns = [
    path('', TaskListView.as_view(), name='tasks_list'),
    path('<int:id>/', TaskDetailView.as_view(), name='task_detail'),
    path('<int:id>/done/', TaskDetailView.completed, name='task_done'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
]
