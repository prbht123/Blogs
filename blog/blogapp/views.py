from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def home(request):
    return render(request,'blog/home.html')

class CreatePost(TemplateView):
    template_name='blog/post/create.html'

class About(TemplateView):
    template_name='blog/about.html'

class Contact(TemplateView):
    template_name='blog/contact.html'

