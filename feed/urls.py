from django.urls import path

from feed.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    CommentCreateView,
    toggle_reaction,
    toggle_repost,
    PostUpdateView,
    PostDeleteView, UserDetailView
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
        toggle_reaction,
        name="toggle-reaction",
    ),
    path(
        "posts/<int:pk>/repost/",
        toggle_repost,
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
        "users/<int:pk>/",
        UserDetailView.as_view(),
        name="user-detail",
    ),
]

app_name = "feed"
