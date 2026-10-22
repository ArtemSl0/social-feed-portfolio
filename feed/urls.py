from django.urls import path

from feed.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    CommentCreateView,
    PostUpdateView,
    PostDeleteView,
    DeleteCommentView,
    ToggleReactionView,
    ToggleRepostView,
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
    path(
        "posts/<int:pk>/react/<str:reaction>/",
        ToggleReactionView.as_view(),
        name="toggle-reaction",
    ),
    path(
        "posts/<int:pk>/repost/",
        ToggleRepostView.as_view(),
        name="toggle-repost",
    ),
    path(
        "posts/<int:pk>/update/",
        PostUpdateView.as_view(),
        name="post-update",
    ),
    path(
        "posts/<int:pk>/delete/",
        PostDeleteView.as_view(),
        name="post-delete",
    ),
    path(
        "comments/<int:pk>/delete/",
        DeleteCommentView.as_view(),
        name="comment-delete",
    ),
]

app_name = "feed"
