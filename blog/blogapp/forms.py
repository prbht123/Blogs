from django import forms
from .models import Post,PostImages


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['title','body','category']


class ImagePostForm(forms.ModelForm):
    class Meta:
        model=PostImages
        fields=['post','image']


class ApprovedForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['status']

class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['title','body','category']