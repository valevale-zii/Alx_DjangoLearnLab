from django import forms
from .models import Post, Comment


class TagWidget(forms.TextInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("attrs", {"placeholder": "Enter tags separated by commas"})
        super().__init__(*args, **kwargs)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]
        widgets = {
            "tags": TagWidget(),   # ✅ Custom widget for tags field
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["author", "content"]
