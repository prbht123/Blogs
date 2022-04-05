
from django.urls import path,include
from . import views


urlpatterns = [
    
    path('', views.home,name='home'),
    path('about/',views.About.as_view()),
    path('contact/',views.Contact.as_view()),
    #path('create/',views.CreatePost.as_view()),
    path('create/',views.AddPostView.as_view()),
    path('bloglist/',views.BlogList.as_view()),
    path('bloglistapi/',views.BlogListApi.as_view()),
    path('blogdetail/<int:pk>/',views.BlogDetailApi.as_view()),
    path('blogdetailview/<slug:slug>',views.DetailedView.as_view())
]
