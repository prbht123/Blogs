
from django.urls import path,include
from . import views

#app_name="blogapp"

urlpatterns = [
    
    path('', views.BlogListApi.as_view(),name = 'home'),
    path('about/',views.About.as_view()),
    path('contact/',views.Contact.as_view()),
    #path('create/',views.CreatePost.as_view()),
    path('create/',views.AddPostView.as_view(),name = 'create_blog'),
    path('edit/<slug:slug>',views.UpdateBlogList.as_view(),name = 'edit_blog'),
    path('delete/<slug:slug>',views.DeleteBlog.as_view(),name = 'delete_blog'),
    path('bloglist/',views.BlogList.as_view()),
    path('bloglistuser/',views.BlogListApiUser.as_view()),
    path('blogdetail/<int:pk>/',views.BlogDetailApi.as_view()),
    path('blogdetailview/<slug:slug>',views.DetailedView.as_view(),name='blog_detail'),
    path('searchblog/',views.SearchBlog.as_view()),
    path('category/',views.CategoryList.as_view(),name='category_detail'),
    path('categorylist/',views.CategoryOnlyList.as_view(),name = 'category_list'),
    path('createcategory/',views.CategoryCreate.as_view(),name = 'create_category'),
    path('updatecategory/<int:pk>',views.CategoryUpdate.as_view(),name = 'update_category'),
    path('deletecategory/<int:pk>',views.CategoryDelete.as_view(),name = 'delete_category'),
    path('taglist/',views.TagsOnlyList.as_view()),
    path('createtag/',views.TagsCreate.as_view()),
    path('updatetag/<int:pk>',views.TagsUpdate.as_view()),
    path('deletetag/<int:pk>',views.TagsDelete.as_view()),
    path('categoryblog/<int:id>',views.CategoryBlogList.as_view()),
    path('images/',views.ImageCreate.as_view()),
    path('approved/<int:pk>/',views.ApprovedByAdmin.as_view()),
    path('approved/',views.ApprovedListView.as_view()),
    path('createcontact/',views.ContactUpload),
]
