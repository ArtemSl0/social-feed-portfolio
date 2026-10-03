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


class PostSearchForm(forms.Form):
    query = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search posts..."}),
    )
