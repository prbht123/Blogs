from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .models import Post
# Create your views here.

def home(request):
    return render(request,'blog/home.html')

class CreatePost(TemplateView):
    template_name='blog/post/create.html'

class About(TemplateView):
    template_name='blog/about.html'

class Contact(TemplateView):
    template_name='blog/contact.html'

class BlogList(TemplateView):
    template_name='blog/post/bloglist.html'


class BlogListApi(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'blog/post/bloglist.html'

    def get(self, request):
        queryset = Post.objects.all()
        return Response({'posts': queryset})