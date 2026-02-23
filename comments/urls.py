from django.urls import path
from comments.views import CommentListCreateView, CommentDetailView

urlpatterns = [
    path("comments/", CommentListCreateView.as_view(), name="comment-list-create"),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="comment-detail"),
]