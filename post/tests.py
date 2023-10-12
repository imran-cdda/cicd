from django.test import TestCase
from .models import Post

class PostTest(TestCase):
    def setUp(self):
        Post.objects.create(title="test")

    def test_title_length(self):
        post = Post.objects.filter(title="test1").first()
        self.assertEqual(post, None)