from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from feed.models import Post


class PostModelTests(TestCase):
    def test_post_str(self):
        user = get_user_model().objects.create_user(
            username="testuser", password="testpass123"
        )
        post = Post.objects.create(author=user, content="Hello world")
        self.assertEqual(str(post), "Hello world - testuser")


class ToggleReactionTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="reactor", password="testpass123"
        )
        self.client.force_login(self.user)
        self.post = Post.objects.create(author=self.user, content="Test post")

    def test_like_creates_reaction(self):
        self.client.post(
            reverse(
                "feed:toggle-reaction",
                kwargs={"pk": self.post.pk, "reaction": "like"},
            )
        )
        self.post.refresh_from_db()
        self.assertEqual(self.post.likes_count, 1)

    def test_like_twice_removes_reaction(self):
        url = reverse(
            "feed:toggle-reaction",
            kwargs={"pk": self.post.pk, "reaction": "like"},
        )
        self.client.post(url)
        self.client.post(url)
        self.post.refresh_from_db()
        self.assertEqual(self.post.likes_count, 0)

    def test_switch_from_like_to_dislike(self):
        self.client.post(
            reverse(
                "feed:toggle-reaction",
                kwargs={"pk": self.post.pk, "reaction": "like"},
            )
        )
        self.client.post(
            reverse(
                "feed:toggle-reaction",
                kwargs={"pk": self.post.pk, "reaction": "dislike"},
            )
        )
        self.post.refresh_from_db()
        self.assertEqual(self.post.likes_count, 0)
        self.assertEqual(self.post.dislikes_count, 1)


class ToggleRepostTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="reposter", password="testpass123"
        )
        self.client.force_login(self.user)
        self.post = Post.objects.create(
            author=self.user, content="Test post"
        )

    def test_repost_creates_record(self):
        self.client.post(
            reverse("feed:toggle-repost", kwargs={"pk": self.post.pk})
        )
        self.post.refresh_from_db()
        self.assertEqual(self.post.reposts_count, 1)

    def test_repost_twice_removes_record(self):
        url = reverse("feed:toggle-repost", kwargs={"pk": self.post.pk})
        self.client.post(url)
        self.client.post(url)
        self.post.refresh_from_db()
        self.assertEqual(self.post.reposts_count, 0)


class AccessControlTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="owner", password="testpass123"
        )
        self.post = Post.objects.create(
            author=self.user, content="Test post"
        )

    def test_anonymous_cannot_create_post(self):
        response = self.client.get(reverse("feed:post-create"))
        self.assertNotEqual(response.status_code, 200)

    def test_anonymous_cannot_toggle_like(self):
        response = self.client.post(
            reverse(
                "feed:toggle-reaction",
                kwargs={"pk": self.post.pk, "reaction": "like"},
            )
        )
        self.assertNotEqual(response.status_code, 200)

    def test_anonymous_can_view_feed(self):
        response = self.client.get(reverse("feed:index"))
        self.assertEqual(response.status_code, 200)
