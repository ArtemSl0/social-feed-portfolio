from django.urls import path

from feed.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    CommentCreateView
)

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/create/", PostCreateView.as_view(), name="post-create"),
    path(
        "posts/<int:pk>/comment/",
        CommentCreateView.as_view(),
        name="comment-create",
    ),
]

app_name = "feed"
