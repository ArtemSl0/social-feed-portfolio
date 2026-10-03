from django import forms
from django.contrib.auth.forms import UserCreationForm

from feed.models import User, Post


class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("bio",)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["content"]
