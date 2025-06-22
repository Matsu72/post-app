from django.test import TestCase
from django.urls import reverse
from posts.models import Post

class PostListViewTest(TestCase):
    def setUp(self):
        Post.objects.create(title="テスト投稿", content="内容")

    def test_get_post_list(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "テスト投稿")
