from django import forms
from django.db import models
from .models import Comment
from .models import Post
class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author=kwargs.pop('author', None)
        super().__init__(*args, **kwargs)
    def save(self, commit=True):
        blog=super().save(commit=False)
        blog.auth=self.author
        blog.save() 
    class Meta:
        model=Post
        fields=("title", "bodyBlog", "image")
class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author=kwargs.pop('author', None)
        self.post=kwargs.pop('post', None)
        super().__init__(*args, **kwargs)
    def save(self, commit=True):
        comment=super().save(commit=False)
        comment.auth=self.author
        comment.post=self.post
        comment.save() 
    class Meta:
        model =Comment
        fields=['body']

