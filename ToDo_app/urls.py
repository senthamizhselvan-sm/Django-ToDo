from django.urls import path
from . import views

urlpatterns = [
    path('add-task' , views.add_task , name = 'add_task'),
    path('completed_task/<int:pk>', views.completed_task , name = 'completed_task'),
    path('incomplete_task/<int:pk>' , views.incomplete_task , name = 'incomplete_task'),
]