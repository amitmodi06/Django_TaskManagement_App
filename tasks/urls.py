from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('completed', views.completed_tasks, name='tasks_completed'),
    path('remaining', views.remaining_tasks, name='tasks_remaining'),
    path('add_task', views.add_task, name='task_add'),
    path('delete_task/<str:task_id>', views.delete_task, name='task_delete'),
    path('detail/<str:task_id>', views.task_detail, name='task_detail'),
    path('toggle_complete/<str:task_id>', views.toggle_complete, name='task_toggle_complete'),
    path('remove_task/<str:task_id>', views.remove_task, name='task_remove'),
]
