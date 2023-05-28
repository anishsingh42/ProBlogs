# forms.py
from django import forms
from .models import Post

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_id', 'title', 'content', 'category_name', 'image_post', 'post_url', 'post_author']
