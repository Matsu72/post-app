from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),# 投稿詳細ページのURL振り分け
    path('new/', views.post_create, name='post_create'),  # ←追加
]