from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content[:30]} - {self.author}"


class PostImage(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="posts/")

    def __str__(self):
        return f"Image for {self.post}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}: {self.post}"


class Like(models.Model):
    LIKE = "like"
    DISLIKE = "dislike"
    REACTION_CHOICES = [
        (LIKE, "Like"),
        (DISLIKE, "Dislike"),
    ]
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="likes"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="likes"
    )
    reaction = models.CharField(max_length=10, choices=REACTION_CHOICES)

    class Meta:
        unique_together = ("user", "post")

    def __str__(self):
        return f"{self.user}: {self.post}, {self.reaction}"


class Repost(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reposts"
    )
    original_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="reposts"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "original_post")

    def __str__(self):
        return f"{self.user}: {self.original_post}"
