from django import forms
from django.contrib.auth.forms import UserCreationForm

from feed.models import User, Post, Comment


class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("bio",)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["content"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
