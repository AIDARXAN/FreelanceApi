from django.urls import path
from .views import *

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('<int:id>/', TaskDetailView.as_view(), name='task_detail'),
    path('<int:id>/accept/', TaskDetailView.accept, name='task_update'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
]