from django.contrib.auth import get_user_model
from django.test import TestCase

from feed.models import Post


class PostModelTests(TestCase):
    def test_post_str(self):
        user = get_user_model().objects.create_user(
            username="testuser", password="testpass123"
        )
        post = Post.objects.create(author=user, content="Hello world")
        self.assertEqual(str(post), "Hello world - testuser")
