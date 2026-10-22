from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("email", "bio", "avatar")
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 3}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["avatar", "bio", "email"]
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 3}),
        }
