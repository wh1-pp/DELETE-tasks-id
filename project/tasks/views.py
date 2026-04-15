from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task

class TaskDeleteView(APIView):
    def delete(self, request, id):
        try:
            task = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return Response(
                {"error": "Задача не найдена"},
                status=status.HTTP_404_NOT_FOUND
            )

        user = request.user

        # Супер-администратор может удалять любые задачи
        if user.is_superuser:
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        # Администратор может удалять только свои задачи
        if user.is_staff:
            if task.owner == user:
                task.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(
                    {"error": "Нет доступа к чужой задаче"},
                    status=status.HTTP_403_FORBIDDEN
                )

        # Обычный пользователь — доступ запрещён
        return Response(
            {"error": "Доступ запрещён"},
            status=status.HTTP_403_FORBIDDEN
        )