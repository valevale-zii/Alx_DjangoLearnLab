from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) < 3:
            raise forms.ValidationError("Comment must be at least 3 characters long.")
        return content
