from django.db import models

 #Postはブログ記事を表すモデルです。
class Post(models.Model):
    #titleは記事のタイトルを表すフィールドです。
    #contentは記事の内容を表すフィールドです。
    #created_atは記事の作成日時を表すフィールドです。
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
