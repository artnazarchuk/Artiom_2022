from django.shortcuts import render
from .models import Post

def blog_index(request):
    posts = Post.objects.order_by('-created_on')
    context = {
        'posts': posts,
    }
    return render(request, 'blog_index.html', context)

def blog_detail(request, pk):
    post_one = Post.objects.get(pk=pk)
    context = {
        'post_one': post_one,
    }
    return render(request, 'blog_detail.html', context)

