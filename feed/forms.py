from django import forms
from django.contrib.auth.forms import UserCreationForm

from feed.models import User, Post, Comment


class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("email", "bio", "avatar")
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 3}),
        }


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class PostForm(forms.ModelForm):
    images = MultipleFileField(
        widget=MultipleFileInput(
            attrs={"multiple": True, "accept": "image/*"}
        ),
        required=False,
    )

    class Meta:
        model = Post
        fields = ["content"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        labels = {"text": ""}
        widgets = {
            "text": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 2,
                    "placeholder": "Write a comment...",
                }
            )
        }

    def clean_text(self):
        text = self.cleaned_data["text"]
        if len(text) > 280:
            raise forms.ValidationError(
                "Comment is too long (max 280 characters)."
            )
        return text


class PostSearchForm(forms.Form):
    query = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search posts..."}),
    )
