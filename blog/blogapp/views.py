from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .models import Post,Category,PostImages
from .serializers import PostSerializers
from rest_framework import status
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from blogapp.forms import BlogPostForm,ImagePostForm,ApprovedForm,BlogUpdateForm
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
        queryset = Post.objects.filter(status='published')
        images= PostImages.objects.all()
        return Response({'posts': queryset,'images':images})

class BlogListApiUser(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'blog/post/bloglist.html'

    def get(self, request):
        if request.user.is_authenticated:
            queryset = Post.objects.filter(author=request.user)
            images = PostImages.objects.all()
            return Response({'posts': queryset,'images':images})
        else:
            return Response({'posts': None})

class AddPostView(CreateView):
    model = Post
    form_class = BlogPostForm
    template_name = 'blog/post/create.html'
    success_url = '/blog/images/'
    def form_valid(self, form):
        user = form.save(commit=False)
        user.author = self.request.user
        user.slug = user.title.lower()
        user.save()
        return redirect('/blog/images/')

    

class UpdateBlogList(UpdateView):
    model = Post
    form_class = BlogUpdateForm
    template_name = 'blog/post/edit.html'
    success_url = '/blog/'
    def get_form_kwargs(self):
        kwargs = super(UpdateBlogList,self).get_form_kwargs()
        kwargs['instance'].status='draft'
        kwargs.update()
        return kwargs
    

class DeleteBlog(DeleteView):
    model = Post
    template_name = 'blog/post/delete.html'
    success_url = '/blog/'

class DetailedView(DetailView):
    model = Post
    #form_class = PostBlogImagesForm
    template_name = 'blog/post/blogdetail.html'
    #context_object_name = 'post'
    def get_context_data(self,*args, **kwargs):
        #title=self.request.GET.get('search')
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.filter(slug=self.object.slug)[0]
        context['images']=PostImages.objects.filter(post=context['post'])
        return context
    

class SearchBlog(ListView):
    """
    Class view functon to handle search 
    """
    template_name = 'blog/post/bloglist.html'
    model=Post
    #context_object_name = 'posts'
    def get_context_data(self, **kwargs):
        title = self.request.GET.get('search')
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(title=title,status='published')
        return context

class SearchBlogUser(ListView):
    template_name = 'blog/post/bloglist.html'
    model=Post
    #context_object_name = 'posts'
    def get_context_data(self, **kwargs):
        title=self.request.GET.get('search')
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(title=title,author=request.user)
        return context


class CategoryList(ListView):
    template_name = 'blog/category/category.html'
    model=Category
    context_object_name = 'categories'
   
class CategoryBlogList(ListView):
    template_name = 'blog/post/bloglist.html'
    model=Post
    #context_object_name = 'posts'
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.kwargs['id'])
        context['posts'] = Post.objects.filter(
            category=self.kwargs['id'],
            status='published')
        context['images'] = PostImages.objects.all()
        return context




class BlogDetailApi(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'blog/post/blogdetail.html'

    def get(self, request):
        queryset = Post.objects.filter(id=1)
        return Response({'posts': queryset})




class ImageCreate(CreateView):
    #model = Post
    form_class = ImagePostForm
    template_name = 'blog/images.html'
    success_url = '/blog/'

class ApprovedByAdmin(UpdateView):
    model=Post
    form_class = ApprovedForm
    template_name = 'blog/admin/approved.html'
    success_url ="/blog/"

class ApprovedListView(ListView):
    template_name = 'blog/admin/approvedhome.html'
    model=Post
    #context_object_name = 'posts'
    def get_context_data(self,*args, **kwargs):
        #title=self.request.GET.get('search')
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(status='draft')
        return context



