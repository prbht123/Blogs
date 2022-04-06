
from django.urls import path,include
from . import views

#app_name="blogapp"

urlpatterns = [
    
    path('', views.BlogListApi.as_view(),name='home'),
    path('about/',views.About.as_view()),
    path('contact/',views.Contact.as_view()),
    #path('create/',views.CreatePost.as_view()),
    path('create/',views.AddPostView.as_view()),
    path('edit/<slug:slug>',views.UpdateBlogList.as_view()),
    path('delete/<slug:slug>',views.DeleteBlog.as_view()),
    path('bloglist/',views.BlogList.as_view()),
    path('bloglistuser/',views.BlogListApiUser.as_view()),
    path('blogdetail/<int:pk>/',views.BlogDetailApi.as_view()),
    path('blogdetailview/<slug:slug>',views.DetailedView.as_view()),
    path('searchblog/',views.SearchBlog.as_view()),
    path('category/',views.CategoryList.as_view()),
    path('categoryblog/<int:id>',views.CategoryBlogList.as_view()),
    path('images/',views.ImageCreate.as_view()),
    path('approved/<int:pk>/',views.ApprovedByAdmin.as_view()),
    path('approved/',views.ApprovedListView.as_view()),
]
