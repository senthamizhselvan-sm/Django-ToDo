from django.urls import path
from . import views

urlpatterns = [
    #add task
    path('add-task' , views.add_task , name = 'add_task'),

    # completed task
    path('completed_task/<int:pk>', views.completed_task , name = 'completed_task'),

    #incomplete tasks
    path('incomplete_task/<int:pk>' , views.incomplete_task , name = 'incomplete_task'),

    #edit task
    path('edit_task/<int:pk>' , views.edit_task , name = 'edit_task'),

    #delete task
    path('delete_task/<int:pk>' , views.delete_task , name = 'delete_task'),
]