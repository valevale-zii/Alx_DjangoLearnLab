from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),

    # Comment CRUD URLs
    path("posts/<int:post_id>/comments/new/", CommentCreateView.as_view(), name="comment-create"),
    path("posts/<int:post_id>/comments/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-update"),
    path("posts/<int:post_id>/comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),
]
