from django.urls import path

from comments.views import CommentDetailView, CommentListCreateView

urlpatterns = [
    path("comments/", CommentListCreateView.as_view(), name="comment-list-create"),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="comment-detail"),
]
