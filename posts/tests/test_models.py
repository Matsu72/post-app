from django.test import TestCase
from posts.models import Post

class PostModelTest(TestCase):
    def test_str_representation(self):
        post = Post(title="テストタイトル")
        self.assertEqual(str(post), "テストタイトル")