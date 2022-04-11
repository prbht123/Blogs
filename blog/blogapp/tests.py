from django.test import TestCase,Client,SimpleTestCase
from django.urls import reverse
from blogapp.models import Blog,Category
from blogapp.forms import BlogPostForm,CategoryForm
from django.contrib.auth.models import User
import json
from django.core.files.uploadedfile import SimpleUploadedFile
import tempfile
# Create your tests here.
def temporary_image():
    import tempfile
    from PIL import Image

    image = Image.new('RGB', (100, 100))
    tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg', prefix="test_img_")
    image.save(tmp_file, 'jpeg')
    tmp_file.seek(0)
    return tmp_file

class TestViews(TestCase):
    def setUp(self):
        """
           This function will be execute firstly from another testing functions. 
        """
        self.client = Client()
        self.list_url = reverse('home')
        self.blog_detail_url = reverse('blog_detail',args = ['blog11'])
        self.create_blog_url = reverse('create_blog')
        self.update_blog_url = reverse('edit_blog',args = ['blog11'])
        self.delete_blog_url = reverse('delete_blog',args = ['blog11'])
        self.category_list_url = reverse('category_list')
        self.create_category_url = reverse('create_category')
        self.update_category_url = reverse('update_category',args = [1])
        self.delete_category_url = reverse('delete_category',args = [1])
        self.user_1 = User.objects.create_user(
            'Chevy Chase', 
            'chevy@chase.com',
             'chevyspassword'
        )
        self.category = Category.objects.create(
            category_name = 'toy',
        
        )
        self.blog11 = Blog.objects.create(
            title = "blog11",
            author = self.user_1,
            body = "hgjhkwkdwa",
            category = self.category

        )

    def test_blog_list_get(self):
        """ 
            This unit testing for listing of blogs.
        """
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/post/bloglist.html')

    def test_blog_detail_get(self):
        """ 
            This unit testing for details of a blog.
        """
        response = self.client.get(self.blog_detail_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/post/blogdetail.html')

    def test_blog_post(self):
        """
            This unit testing for creating new blog.
        """
        response = self.client.post(self.create_blog_url,{
            'title' : "blog12",
            'author' : self.user_1,
            'body' : "hgjhkwkdwa",
            'category' : self.category
        })
        self.assertEquals(response.status_code,200)
        #self.assertEquals(self.blog11.title,'blog12')
        self.assertTemplateUsed(response,'blog/post/create.html')

    def test_blog_update(self):
        """
            This unit testing for updating of exsting blog.
        """
        response = self.client.put(self.update_blog_url,{
            'title' : "blog112",
            'author' : self.user_1,
            'body' : "hsdgkjfbwkfjbwaj",
            'category' : self.category
        })
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/post/edit.html')

    def test_blog_delete(self):
        """
            This unit testing for deleting of existing blog.
        """        
        response = self.client.delete(self.delete_blog_url)
        # self.assertEquals(response.status_code,200)
        # self.assertTemplateUsed(response,'blog/post/delete.html')   
        self.assertRedirects(response, '/blog/', status_code=302,target_status_code=200, fetch_redirect_response=True)
     



    def test_category_list_get(self):
        """ 
            This unit testing for listing of categories.
        """
        response = self.client.get(self.category_list_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/category/listcategory.html')


    def test_category_update(self):
            """
                This function is for testing of updating a particular category.
            """
            response = self.client.put(self.update_category_url,{
                'title' : "toy1",
                'description' : "vjavshbajs"
            })
            self.assertEquals(response.status_code,200)
            self.assertTemplateUsed(response,'blog/category/categoryedit.html')

    def test_category_delete(self):
        """
            This function for testing of deleting a particular category.
        """
        response = self.client.delete(self.delete_category_url,json.dumps({
            'id' : 1
        }))
        self.assertRedirects(response, '/blog/', status_code=302,target_status_code=200, fetch_redirect_response=True)


    def test_category_post(self):
        """
            This unit testing for creating of one category.
        """
        response = self.client.post(self.create_category_url,{
            'category_name' : "Stone",
            'descripton' : "nice to one",
            'image' : temporary_image()
            #'image' : SimpleUploadedFile(name='music1.jpg', content=open('/home/prabhat/Downloads', 'rb').read(), content_type='image/jpg')
            #'image' : tempfile.NamedTemporaryFile(suffix=".jpg").name
        },format="multipart")
        #self.assertEquals(response.status_code,200)
        #self.assertEquals(self.category.Category.first().category_name,'Stone')
        #self.assertTemplateUsed(response,'blog/category/addcategory.html')
        self.assertRedirects(response, '/blog/', status_code=302,target_status_code=200, fetch_redirect_response=True)

        


    ##   Model testing.......................
    def test_blog_slug_module(self):
        """
            Testing for Blog module.
        """
        self.assertEquals(self.blog11.slug,'blog11')

    def test_category_slug_module(self):
        """
            Testing for Category module.
        """
        self.assertEquals(self.category.slug,'toy')

   
