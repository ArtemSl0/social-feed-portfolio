from django.urls import path

from feed.views import (
    PostListView,
    PostDetailView,
    PostCreateView
)

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/create/", PostCreateView.as_view(), name="post-create"),
]

app_name = "feed"
