from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),# 投稿詳細ページのURL振り分け
    #path('new/', views.post_create, name='post_create'),  # 新規投稿ページのURL振り分け
    #path('<int:pk>/edit/', views.post_edit, name='post_edit'),# 投稿編集ページのURL振り分け
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),  # 投稿削除ページのURL振り分け
    path('new/', views.post_create_form, name='post_create'),# ModelForm版 新規投稿ページのURL振り分け
    path('<int:pk>/edit/', views.post_edit_form, name='post_edit'),# ModelForm版 投稿編集ページのURL振り分け
]