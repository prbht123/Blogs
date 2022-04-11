from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .models import Blog,Category,PostImages,Contact,Tag
from .serializers import PostSerializers
from rest_framework import status
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from blogapp.forms import BlogPostForm,ImagePostForm,ApprovedForm,BlogUpdateForm,CategoryForm,TagsForm
# Create your views here.
from django.core.mail import send_mail
from django.utils import timezone

def home(request):
    return render(request,'blog/home.html')

class CreatePost(TemplateView):
    template_name = 'blog/post/create.html'

class AddedPost(APIView):
    def post(self,request):
        print(request.data)
        pass

class About(TemplateView):
    template_name = 'blog/about.html'

class Contact(TemplateView):
    template_name = 'blog/contact.html'

class BlogList(TemplateView):
    template_name = 'blog/post/bloglist.html'

class BlogListApi(APIView):
    """
        This class is used for showing all blogs.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'blog/post/bloglist.html'
    def get(self, request):
        queryset = Blog.objects.filter(status='published')
        images = PostImages.objects.all()
        categories = Category.objects.all()
        return Response({'posts': queryset,'images':images,'categories':categories})

class BlogListApiUser(APIView):
    """
        This class is used for showing all blogs for login user.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'blog/post/bloglist.html'
    def get(self, request):
        if request.user.is_authenticated:
            queryset = Blog.objects.filter(author=request.user)
            images = PostImages.objects.all()
            categories = Category.objects.all()
            return Response({'posts': queryset,'images':images,'categories':categories})
        else:
            return Response({'posts': None})

class AddPostView(CreateView):
    """
        This class is used for adding new blog.
    """
    model = Blog
    form_class = BlogPostForm
    template_name = 'blog/post/create.html'
    success_url = '/blog/'
    def form_valid(self, form):
        user = form.save(commit=False)
        user.author = self.request.user
        print(user.author)
        #user.slug = user.title.lower()
        user.save()
        return redirect('/blog/')

class UpdateBlogList(UpdateView):
    """
        This class is used for updating of a particular blog.
    """
    model = Blog
    form_class = BlogPostForm            #BlogUpdateForm  
    template_name = 'blog/post/edit.html'
    success_url = '/blog/'
    def get_form_kwargs(self):
        kwargs = super(UpdateBlogList,self).get_form_kwargs()
        kwargs['instance'].status='draft'
        kwargs.update()
        return kwargs
    
class DeleteBlog(DeleteView):
    """
        This class is used for deleting a particular blog.
    """
    model = Blog
    template_name = 'blog/post/delete.html'
    success_url = '/blog/'

class DetailedView(DetailView):
    """
        This class is used for showing a particular blog's detail.
    """
    model = Blog
    #form_class = PostBlogImagesForm
    template_name = 'blog/post/blogdetail.html'
    #context_object_name = 'post'
    def get_context_data(self,*args, **kwargs):
        #title=self.request.GET.get('search')
        context = super().get_context_data(**kwargs)
        context['post'] = Blog.objects.filter(slug=self.object.slug)[0]
        context['images'] = PostImages.objects.filter(post=context['post'])
        #print(context['post'].category)
        context['related_blog'] = Blog.objects.filter(category = context['post'].category).exclude(id = context['post'].id)
        return context
    
class SearchBlog(ListView):
    """
    Class view functon to handle search 
    """
    template_name = 'blog/post/bloglist.html'
    model=Blog
    #context_object_name = 'posts'
    def get_context_data(self, **kwargs):
        title = self.request.GET.get('search')
        context = super().get_context_data(**kwargs)
        context['posts'] = Blog.objects.filter(title = title,status = 'published')
        context['categories'] = Category.objects.all()
        return context

class SearchBlogUser(ListView):
    """
        This class is used for searching blogs of login user's blog only.
    """
    template_name = 'blog/post/bloglist.html'
    model = Blog
    #context_object_name = 'posts'
    def get_context_data(self, **kwargs):
        title = self.request.GET.get('search')
        context = super().get_context_data(**kwargs)
        context['posts'] = Blog.objects.filter(title = title,author = request.user)
        return context

class CategoryList(ListView):
    """
        This class is used for showing all categories.
    """
    template_name = 'blog/category/category.html'
    model = Category
    context_object_name = 'categories'
   
class CategoryBlogList(ListView):
    template_name = 'blog/post/bloglist.html'
    model = Blog
    #context_object_name = 'posts'
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.kwargs['id'])
        context['posts'] = Blog.objects.filter(
            category=self.kwargs['id'],
            status='published')
        context['images'] = PostImages.objects.all()
        return context

class BlogDetailApi(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'blog/post/blogdetail.html'
    def get(self, request):
        queryset = Blog.objects.filter(id = 1)
        return Response({'posts': queryset})

class ImageCreate(CreateView):
    #model = Post
    form_class = ImagePostForm
    template_name = 'blog/images.html'
    #success_url = '/blog/'
    def form_valid(self, form):
        data = form.save(commit=False)
        data.image = self.request.FILES['image']
        data.save()
        return redirect('/blog/')

class ApprovedByAdmin(UpdateView):
    model = Blog
    form_class = ApprovedForm
    template_name = 'blog/admin/approved.html'
    success_url ="/blog/"
    def get_form_kwargs(self):
        kwargs = super(ApprovedByAdmin,self).get_form_kwargs()
        kwargs['instance'].publish = timezone.now()
        kwargs.update()
        return kwargs

class ApprovedListView(ListView):
    template_name = 'blog/admin/approvedhome.html'
    model = Blog
    #context_object_name = 'posts'
    def get_context_data(self,*args, **kwargs):
        #title=self.request.GET.get('search')
        context = super().get_context_data(**kwargs)
        context['posts'] = Blog.objects.filter(status = 'draft')
        return context

def ContactUpload(request):
    if request.method == 'POST':
        gg = Contact.objects.all()
        obj = Contact(
        name = request.POST.get('name'),
        email = request.POST.get('email'),
        mobile_number = request.POST.get('mobile_number'),
        messages = request.POST.get('messages')
        )
        obj.save()
        cd={
            'to':'Admin123@YOPmail.com'
        }
        send_mail("subject", "message",request.POST.get('email'),[cd['to']])
        return redirect('/blog/')

class CategoryOnlyList(ListView):
    model = Category
    template_name = 'blog/category/listcategory.html'
    context_object_name = 'categories'

class CategoryCreate(CreateView):
    form_class = CategoryForm
    template_name = 'blog/category/addcategory.html'
    #success_url = '/blog/'
    def form_valid(self, form):
        data = form.save(commit=False)
       # data.slug = data.category_name.lower()
        data.image = self.request.FILES['image']
        data.save()
        return redirect('/blog/')

class CategoryDelete(DeleteView):
    model = Category
    template_name = 'blog/post/delete.html'
    success_url = '/blog/'

class CategoryUpdate(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'blog/category/categoryedit.html'
    #success_url = '/blog/'
    def form_valid(self, form):
        data = form.save(commit=False)
        #data.slug = data.category_name.lower()
        data.image = self.request.FILES['image']
        data.save()
        return redirect('/blog/')

class TagsCreate(CreateView):
    form_class = TagsForm
    template_name = 'blog/tag/tags.html'
    #success_url = '/blog/'
    def form_valid(self, form):
        data = form.save(commit=False)
        data.slug = data.name.lower()
        data.save()
        return redirect('/blog/')

class TagsDelete(DeleteView):
    model = Tag
    template_name = 'blog/post/delete.html'
    success_url = '/blog/'

class TagsUpdate(UpdateView):
    model = Tag
    form_class = TagsForm
    template_name = 'blog/tag/tagedit.html'
    success_url = '/blog/'
    def get_form_kwargs(self):
        kwargs = super(TagsUpdate,self).get_form_kwargs()
        #kwargs['instance'].status='draft'
        kwargs.update()
        return kwargs

class TagsOnlyList(ListView):
    model = Tag
    template_name = 'blog/tag/listtag.html'
    context_object_name = 'tags'


    
