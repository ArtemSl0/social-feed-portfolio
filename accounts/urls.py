from django.urls import path

from accounts.views import RegisterView, UserDetailView, ProfileUpdateView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path(
        "users/<int:pk>/", UserDetailView.as_view(), name="user-detail"
    ),
    path(
        "profile/edit/",
        ProfileUpdateView.as_view(),
        name="profile-update",
    ),
]

app_name = "accounts"
