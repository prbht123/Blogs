from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializers
from rest_framework import status
from django.views.generic import ListView,CreateView,DetailView
from blogapp.forms import BlogPostForm
# Create your views here.


def home(request):
    return render(request,'blog/home.html')



class CreatePost(TemplateView):
    template_name='blog/post/create.html'

class AddedPost(APIView):
    def post(self,request):
        print(request.data)
        pass

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
        print("helloooo")
        return Response({'posts': queryset})



class AddPostView(CreateView):
    model = Post
    form_class = BlogPostForm
    template_name = 'blog/post/create.html'
    success_url = '/blog/bloglistapi'


class DetailedView(DetailView):
    model = Post
    template_name = 'blog/post/blogdetail.html'
    context_object_name = 'post'

class BlogDetailApi(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'blog/post/blogdetail.html'

    def get(self, request):
        print(id)
        print(request.data)
        queryset = Post.objects.filter(id=1)
        return Response({'posts': queryset})

# class CreatePost(APIView):
#     # renderer_classes = [TemplateHTMLRenderer]
#     # template_name = 'blog/post/createserial.html'
#     def post(self, request, *args, **kwargs):
#         print(request.data)
#         serializer = PostSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             #return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return render(request,'blog/home.html')

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

