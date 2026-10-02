from django.urls import path

from feed.views import PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
]

app_name = "feed"
