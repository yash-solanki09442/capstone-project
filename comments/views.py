from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.permissions import IsOwnerOrReadOnly
from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
