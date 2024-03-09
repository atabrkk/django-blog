from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Category, Blog


# Create your views here.

def posts_by_category(request, category_slug):
    posts = Blog.objects.filter(status='Published', category__category_slug=category_slug)
    category = get_object_or_404(Category, category_slug=category_slug)
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'posts_by_category.html', context)


def blog(request, slug):
    single_blog = get_object_or_404(Blog, status='Published', slug=slug)
    context = {
        'single_blog': single_blog
    }
    return render(request, 'blog.html', context)


def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(
        Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword),
        status='Published')
    context = {
        'blogs': blogs,
        'keyword': keyword
    }
    return render(request, 'search.html', context)
