from django.shortcuts import render, get_object_or_404

from .models import Post


def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', locals())


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', locals())


def taki(request):
    post = get_object_or_404(Post, pk=1)
    return render(request, 'blog/TAKI.html', locals())
