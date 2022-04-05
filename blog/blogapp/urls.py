
from django.urls import path,include
from . import views


urlpatterns = [
    
    path('', views.BlogListApi.as_view(),name='home'),
    path('about/',views.About.as_view()),
    path('contact/',views.Contact.as_view()),
    #path('create/',views.CreatePost.as_view()),
    path('create/',views.AddPostView.as_view()),
    path('bloglist/',views.BlogList.as_view()),
    path('bloglistuser/',views.BlogListApiUser.as_view()),
    path('blogdetail/<int:pk>/',views.BlogDetailApi.as_view()),
    path('blogdetailview/<slug:slug>',views.DetailedView.as_view()),
    path('searchblog/',views.SearchBlog.as_view()),
    path('category/',views.CategoryList.as_view()),
    path('categoryblog/<slug:slug>',views.CategoryBlogList.as_view())
]
