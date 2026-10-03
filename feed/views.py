from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy

from feed.forms import UserRegistrationForm, PostForm, CommentForm
from feed.models import Post, User, Comment, Like, Repost


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        return context


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


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "feed:post-detail", kwargs={"pk": self.kwargs["pk"]}
        )


@login_required
def toggle_reaction(request, pk, reaction):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(
        user=request.user, post=post, defaults={"reaction": reaction}
    )
    if not created:
        if like.reaction == reaction:
            like.delete()
        else:
            like.reaction = reaction
            like.save()
    return redirect("feed:post-detail", pk=pk)


@login_required
def toggle_repost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    repost = Repost.objects.filter(
        user=request.user, original_post=post
    ).first()
    if repost:
        repost.delete()
    else:
        Repost.objects.create(user=request.user, original_post=post)
    return redirect("feed:post-detail", pk=pk)
