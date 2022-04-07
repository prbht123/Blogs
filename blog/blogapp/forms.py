from django import forms
from .models import Blog,PostImages,Contact,Category,Tag


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body','category']


class ImagePostForm(forms.ModelForm):
    class Meta:
        model = PostImages
        fields = ['post','image']


class ApprovedForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['status']

class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body','category']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name','image','description']
        widgets = {
            'category_name': forms.TextInput(attrs={'placeholder': 'Category Name','class':'form-control mb-4'}),
            'description': forms.TextInput(attrs={'placeholder': 'description','class':'form-control mb-4'}),
        }


class TagsForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name','class':'form-control mb-4'}),
              }

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = ['name','email','mobile_number','messages']