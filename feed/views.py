from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from feed.forms import UserRegistrationForm, PostForm
from feed.models import Post, User


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post


class RegisterView(generic.CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("feed:index")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
