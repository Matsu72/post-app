#HTMLを生成して返す
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})


def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Post.objects.create(title=title, content=content)
            return redirect('post_list')  # 投稿後は一覧に戻る
    return render(request, 'posts/post_form.html')

