from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=100)
    slug= models.SlugField(max_length=250)
    image = models.ImageField(upload_to='blog/category/images/',blank=True,null=True)
    description = models.CharField(max_length=500, null=True,blank=True, verbose_name='Description')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.category_name

class Tag(models.Model):

    name  = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name 


class Blog(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User,on_delete = models.CASCADE,related_name='blog_posts')
    body = models.TextField()
    category = models.ForeignKey(Category,on_delete = models.CASCADE,related_name='category_posts')
    image = models.ImageField(upload_to='blog/images/',blank=True,null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title




class PostImages(models.Model):
    post = models.ForeignKey(Blog,on_delete = models.CASCADE,related_name='image_posts')
    image = models.ImageField(upload_to='blog/images/',blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title

class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='Name')
    email = models.EmailField(null=True)
    mobile_number = models.BigIntegerField()
    messages = models.TextField()
    def __str__(self):
        return f"{ self.name }" 
