from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import UserRegistrationForm, ProfileUpdateForm
from accounts.models import User


class RegisterView(generic.CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"


class UserDetailView(generic.DetailView):
    model = User
    context_object_name = "profile_user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = self.object.posts.select_related(
            "author"
        ).order_by("-created_at")
        context["reposts"] = self.object.reposts.select_related(
            "original_post__author"
        ).order_by("-created_at")
        return context


class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = "accounts/profile_form.html"

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy(
            "accounts:user-detail", kwargs={"pk": self.request.user.pk}
        )
