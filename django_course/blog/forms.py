from django.forms import ModelForm
from .models import Blog, Comment
from django import forms

class BlogModelForm(ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "content", "image"]

    def __init__(self, *args, **kwargs):
        super(BlogModelForm, self).__init__(*args, **kwargs)
        self.fields["title"].help_text=""
        self.fields["title"].label=""
        self.fields["title"].widget=forms.Textarea(
            attrs={
                "placeholder":"Название блога",
                "rows": 1,
                "class": "form-control",
            }
        )

        self.fields["content"].help_text=""
        self.fields["content"].label=""
        self.fields["content"].widget=forms.Textarea(
            attrs={
                "placeholder":"Содержание",
                "rows": 10,
                "class": "form-control",
            }
        )

class CommentModelForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]

    def __init__(self, *args, **kwargs):
        super(CommentModelForm, self).__init__(*args, **kwargs)
        self.fields["text"].help_text=""
        self.fields["text"].label=""
        self.fields["text"].widget=forms.Textarea(
            attrs={
                "placeholder":"Текст комментария",
                "rows": 1,
                "class": "form-control",
            }
        )  
