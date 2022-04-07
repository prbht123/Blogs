from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Blog,Category




class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields=['id','title','slug','body','status','author','category',]


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields=['id','category_name','slug']