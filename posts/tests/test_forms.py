# posts/tests/test_forms.py
from django.test import TestCase
from posts.forms import PostForm

class PostFormTest(TestCase):
    def test_valid_data(self):
        form = PostForm(data={
            'title': 'テストタイトル',
            'content': 'これはテストの内容です。'
        })
        self.assertTrue(form.is_valid())  # ✅ バリデーションOK

    def test_missing_title(self):
        form = PostForm(data={
            'title': '',  # ❌ タイトルが空
            'content': '内容あり'
        })
        self.assertFalse(form.is_valid())  # ✅ バリデーションNG
        self.assertIn('title', form.errors)

    def test_missing_content(self):
        form = PostForm(data={
            'title': 'タイトルあり',
            'content': ''  # ❌ 内容が空
        })
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors)
