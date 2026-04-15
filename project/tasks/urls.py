from django.urls import path
from .views import TaskDeleteView

urlpatterns = [
    path('tasks/<int:id>/', TaskDeleteView.as_view(), name='task-delete'),
]