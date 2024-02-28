from django.shortcuts import render, get_object_or_404
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