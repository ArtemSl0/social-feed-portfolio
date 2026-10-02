from django.views import generic

from feed.models import Post


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
