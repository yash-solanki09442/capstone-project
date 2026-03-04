from django.db import transaction
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.permissions import IsOwnerOrReadOnly
from tasks.models import Task
from tasks.serializers import TaskSerializer

from .realtime import broadcast_event


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        instance = serializer.save()

        event = {
            "type": "task.updated",
            "task_id": instance.id,
            "project_id": instance.project_id,
            "payload": serializer.data,
            "ts": (
                instance.updated_at.isoformat()
                if hasattr(instance, "updated_at")
                else None
            ),
        }

        transaction.on_commit(lambda: broadcast_event(event))
