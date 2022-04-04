
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('', views.home),
    path('about/',views.About.as_view()),
    path('contact/',views.Contact.as_view()),
    path('create/',views.CreatePost.as_view()),
    path('bloglist/',views.BlogList.as_view()),
    path('bloglistapi/',views.BlogListApi.as_view()),
]
