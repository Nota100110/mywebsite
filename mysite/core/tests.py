from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.urls import reverse
from blog.models import Post, Comment
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import PostForm, CommentForm

class BlogAppTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(
            title='Test Post',
            image='This is a test post image',
            intro='This is a test post intro',
            body='This is a test post body',
            published_date=timezone.now()
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author='Test Commenter',
            text='This is a test comment text',
            created_date=timezone.now(),
            approved_comment=True
        )

    def test_frontpage_view(self):
        response = self.client.get(reverse('frontpage'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertTemplateUsed(response, 'core/frontpage.html')

    def test_blog_view(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertTemplateUsed(response, 'core/blog.html')

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertTemplateUsed(response, 'core/post_list.html')

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertTemplateUsed(response, 'core/post_detail.html')

    def test_post_new_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('post_new', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/post_edit.html')

    # Add more tests for other views as needed

    def test_add_comment_to_post_view(self):
        response = self.client.get(reverse('add_comment_to_post', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/add_comment_to_post.html')

    def test_comment_approve_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('comment_approve', args=[self.comment.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Comment.objects.get(pk=self.comment.pk).approved_comment)

    def test_comment_remove_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('comment_remove', args=[self.comment.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRaises(Comment.DoesNotExist, Comment.objects.get, pk=self.comment.pk)

#    def test_about_view(self):
#        response = self.client.get(reverse('about'))
#        self.assertEqual(response.status_code, 200)
#        self.assertTemplateUsed(response, 'core/about.html')

#     def test_coming_soon_page_view(self):
#        response = self.client.get(reverse('coming_soon_page'))
#        self.assertEqual(response.status_code, 200)
#        self.assertTemplateUsed(response, 'core/coming_soon_page.html')